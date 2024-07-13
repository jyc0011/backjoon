import sys

def calc(n, k, coins):
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for coin in coins:
        for amount in range(coin, k + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[k]

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

print(calc(n, k, coins))