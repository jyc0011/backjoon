import sys

input = sys.stdin.readline

hex_nums = []
n = 1

while True:
    h = n * (2 * n - 1)
    if h > 1000000:
        break
    hex_nums.append(h)
    n += 1

N = int(input())
dp = [float('inf')] * (N + 1)
dp[0] = 0

for h in hex_nums:
    for i in range(h, N + 1):
        if dp[i - h] + 1 < dp[i]:
            dp[i] = dp[i - h] + 1

print(dp[N])