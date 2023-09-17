N = int(input())
heights = list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(N, 0, -1):
    if i + heights[i - 1] + 1 <= N:
        dp[i] = dp[i + heights[i - 1] + 1] + 1
    else:
        dp[i] = 1

print(" ".join(map(str, dp[1:])))