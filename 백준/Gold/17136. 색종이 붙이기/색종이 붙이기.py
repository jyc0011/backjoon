import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]

ans = float('inf')

def can_attach(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] == 0:
                return False
    return True

def attach(x, y, size, value):
    for i in range(x, x+size):
        for j in range(y, y+size):
            board[i][j] = value

def dfs(idx, used):
    global ans
    if used >= ans:
        return
    if idx == 100:
        ans = min(ans, used)
        return
    x = idx // 10
    y = idx % 10
    if board[x][y] == 0:
        dfs(idx+1, used)
    else:
        for size in range(5, 0, -1):
            if papers[size] > 0 and can_attach(x, y, size):

                attach(x, y, size, 0)
                papers[size] -= 1
                dfs(idx+1, used+1)
                attach(x, y, size, 1)
                papers[size] += 1
dfs(0, 0)
print(ans if ans != float('inf') else -1)