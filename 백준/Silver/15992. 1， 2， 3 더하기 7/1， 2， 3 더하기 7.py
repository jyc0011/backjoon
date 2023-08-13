import sys

dp = [[0] * 1001 for _ in range(1001)]
MOD = 1000000009
dp[1][1] = dp[2][1] = dp[3][1] = 1
for i in range(2, 1001) :
    for j in range(1, 1001) :
        for k in range(1, 4) :
            if j - k > 0 :
                dp[j][i] += dp[j - k][i - 1]
            dp[j][i] %= MOD
for _ in range(int(sys.stdin.readline())) :
    n, m = map(int, sys.stdin.readline().split())
    print(dp[n][m])