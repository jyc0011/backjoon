import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    a[x][y] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
                cnt += 1
                a[nx][ny] = 0
                q.append((nx, ny))
    return cnt

ans1 = 0
ans2 = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            ans1 += 1
            ans2 = max(ans2, bfs(i, j))

print(ans1)
print(ans2)