import sys
MAX = 100000
MOD = 1000000009
EVEN = 0
ODD = 1

dp = [None for _ in range(4)]
dp[0] = [0, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]
dp[3] = [2, 2]

for ii in range(4, MAX + 1):
    dp.append([
            (dp[ii-1][ODD] + dp[ii-2][ODD] + dp[ii-3][ODD]) % MOD,
            (dp[ii-1][EVEN] + dp[ii-2][EVEN] + dp[ii-3][EVEN]) % MOD
            ])

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    current = int(sys.stdin.readline())
    print(dp[current][ODD], dp[current][EVEN])