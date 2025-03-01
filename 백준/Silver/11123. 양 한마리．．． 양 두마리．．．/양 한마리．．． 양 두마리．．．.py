import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
d=[(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(x, y):
    grid[x][y] = '.'
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '#':
            dfs(nx, ny)

T = int(input().strip())
for _ in range(T):
    H, W = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]
    count = 0
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                count += 1
                dfs(i, j)
    
    print(count)