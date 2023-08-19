import sys

from collections import deque

n, m = map(int, sys.stdin.readline().split())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

queue = deque()
dist = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if space[i][j] == 1:
            queue.append((i, j))
            dist[i][j] = 0

while queue:
    x, y = queue.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

max_safe_distance = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] > max_safe_distance:
            max_safe_distance = dist[i][j]

print(max_safe_distance)