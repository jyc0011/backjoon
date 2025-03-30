import sys

input=sys.stdin.readline

def calc(n, m):
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for j in range(m):
        dp[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]

N, M, K = map(int, input().split())
if K == 0:
    print(calc(N, M))
    sys.exit()

K -= 1
row_m, col_m = divmod(K, M)
first = calc(row_m + 1, col_m + 1)
second = calc(N - row_m, M - col_m)
print(first * second)