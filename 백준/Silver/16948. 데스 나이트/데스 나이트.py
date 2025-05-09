import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
r1, c1, r2, c2 = map(int, input().split())

if (r1, c1) == (r2, c2):
    print(0)
    sys.exit(0)

moves = [(-2, -1), (-2, +1), (0, -2), (0, +2), (+2, -1), (+2, +1)]

dist = [[-1] * N for _ in range(N)]
dist[r1][c1] = 0
q = deque([(r1, c1)])

while q:
    r, c = q.popleft()
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            if (nr, nc) == (r2, c2):
                print(dist[nr][nc])
                sys.exit(0)
            q.append((nr, nc))

print(-1)