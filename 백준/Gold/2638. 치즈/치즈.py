import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and cheese[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif cheese[nx][ny] == 1:
                    visited[nx][ny] += 1

n, m = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0

while any(1 in row for row in cheese):
    visited = [[0] * m for _ in range(n)]
    bfs(0, 0)
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1 and visited[i][j] >= 2:
                cheese[i][j] = 0
    cnt += 1

print(cnt)