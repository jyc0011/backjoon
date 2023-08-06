from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = '.'
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < m) and (0 <= X < n) and graph[Y][X] == '#':
                q.append((Y, X))
                graph[Y][X] = '.'

m, n = map(int, input().split())
graph = [list(input()) for _ in range(m)]
d = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == '#':
            bfs(i, j)
            cnt += 1
print(cnt)