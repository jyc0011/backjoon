def dp(grid):
    N = len(grid)
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = grid[0][0]
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] * 2 + grid[0][j]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] * 2 + grid[i][0]
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) * 2 + grid[i][j]
    return dp[N-1][N-1]

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
print(dp(grid))