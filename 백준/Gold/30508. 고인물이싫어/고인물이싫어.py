import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
h, w = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

K = int(input())
drains = []
for _ in range(K):
    r, c = map(int, input().split())
    drains.append((r - 1, c - 1))
    
safe = [[False] * M for _ in range(N)]
q = deque()

for r, c in drains:
    safe[r][c] = True
    q.append((r, c))

while q:
    r, c = q.popleft()
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < N and 0 <= nc < M:
            if not safe[nr][nc] and grid[nr][nc] >= grid[r][c]:
                safe[nr][nc] = True
                q.append((nr, nc))
                
ps = [[0] * (M + 1) for _ in range(N + 1)]
for r in range(N):
    for c in range(M):
        water = 1 if not safe[r][c] else 0
        ps[r + 1][c + 1] = ps[r][c + 1] + ps[r + 1][c] - ps[r][c] + water

answer = 0
for r1 in range(N - h + 1):
    for c1 in range(M - w + 1):
        r2 = r1 + h - 1
        c2 = c1 + w - 1
        temp = ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1]  - ps[r2 + 1][c1]+ ps[r1][c1]
        if temp == 0:
            answer += 1

print(answer)