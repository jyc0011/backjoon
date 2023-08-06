import sys
sys.setrecursionlimit(3000000)

def dfs(y, x):
    graph[y][x] = '*'
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < m) and (0 <= X < n) and graph[Y][X] == '@':
            dfs(Y, X)
            
while 1:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    graph = [list(input()) for _ in range(m)]
    d = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == '@':
                dfs(i, j)
                cnt += 1
    print(cnt)