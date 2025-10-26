import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 10007
dp = [[0] * (N + 1) for _ in range(N + 1)]
for n in range(N + 1):
    dp[n][0] = 1
    dp[n][n] = 1
    for k in range(1, n):
        dp[n][k] = (dp[n-1][k-1] + dp[n-1][k]) % MOD

print(dp[N][K])