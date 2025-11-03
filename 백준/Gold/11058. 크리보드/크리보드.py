import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = dp[i - 1] + 1
    for j in range(1, i - 2):
        paste = i - j - 1
        current = dp[j] * paste
        dp[i] = max(dp[i], current)

print(dp[N])