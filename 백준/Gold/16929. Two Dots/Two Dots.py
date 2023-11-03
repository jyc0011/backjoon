import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, px, py, c):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == c:
            if not (nx == px and ny == py) and visited[nx][ny]:
                return True
            if not visited[nx][ny] and dfs(nx, ny, x, y, c):
                return True
    return False

n, m = map(int, sys.stdin.readline().rstrip().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j, -1, -1, board[i][j]):
                print("Yes")
                exit()

print("No")