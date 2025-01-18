import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,k=map(int, input().rstrip().split())
coins=[int(input()) for _ in range(n)]
dp = [0]+[float('inf')] * (k)

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
        
print(dp[k] if dp[k] != float('inf') else -1)