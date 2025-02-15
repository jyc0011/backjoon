import sys
from collections import deque

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start_x, start_y, grid, visited, M, N):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    area_size = 1
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                area_size += 1
    
    return area_size

M, N, K = map(int, sys.stdin.readline().split())
grid = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

visited = [[False] * N for _ in range(M)]
areas = []

for i in range(M):
    for j in range(N):
        if grid[i][j] == 0 and not visited[i][j]:
            areas.append(bfs(i, j, grid, visited, M, N))
    
areas.sort()
print(len(areas))
print(" ".join(map(str, areas)))