def calc(n, s):
    dp = [0] * n
    dp[0] = s[0]
    for i in range(1, n):
        dp[i] = max(s[i], dp[i-1] + s[i])
    return max(dp)

n = int(input())
s = list(map(int, input().split()))

print(calc(n, s))