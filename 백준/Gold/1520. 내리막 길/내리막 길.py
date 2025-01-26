import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y):
    if x == M - 1 and y == N - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and li[x][y] > li[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]

M,N=map(int, input().rstrip().split())
li=[list(map(int, input().rstrip().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
H=dfs(0,0)

print(H)