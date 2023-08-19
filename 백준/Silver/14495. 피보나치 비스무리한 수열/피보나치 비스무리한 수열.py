import sys

N = int(input().strip())

dp = [0, 1, 1]

for i in range(3, N + 1):
    dp.append(dp[i - 1] + dp[i - 3])

print(dp[N])