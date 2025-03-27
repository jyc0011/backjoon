import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pages = set(list(map(int, input().split())))

dp = [0] * (N+2)

for i in range(N, 0, -1):
    if i in pages:
        skip = dp[i+1]
        cost = float('inf')
        for j in range(i, N+1):
            cost = min(cost, 5 + 2*(j - i + 1) + dp[j+1])
        dp[i] = min(skip, cost)
    else:
        cost = float('inf')
        for j in range(i, N+1):
            cost = min(cost, 5 + 2*(j - i + 1) + dp[j+1])
        dp[i] = cost

print(dp[1])