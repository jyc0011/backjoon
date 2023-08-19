N = int(input())

dp = [False] * (N+1)

for i in range(1, N+1):
    if i-1 >= 0 and not dp[i-1]:
        dp[i] = True
    elif i-3 >= 0 and not dp[i-3]:
        dp[i] = True
    elif i-4 >= 0 and not dp[i-4]:
        dp[i] = True

if dp[N]:
    print("SK")
else:
    print("CY")