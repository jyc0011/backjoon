import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    people_count = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if campus[nx][ny] == 'P':
                    people_count += 1
                if campus[nx][ny] != 'X':
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return people_count if people_count > 0 else "TT"

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, sys.stdin.readline().rstrip().split())
campus = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            x, y = i, j
            break

print(bfs(x, y))