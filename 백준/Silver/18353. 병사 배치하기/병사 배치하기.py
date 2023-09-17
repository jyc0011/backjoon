import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_len = max(dp)
result = n - max_len
print(result)