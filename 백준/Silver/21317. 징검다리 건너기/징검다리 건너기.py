import sys

def min_energy(n, m, k):
    if n == 1: return 0
    if n == 2: return m[0][0]

    dp = [0]*n
    dp[1] = m[0][0]
    dp[2] = min(m[0][0] + m[1][0], m[0][1])

    for i in range(3, n):
        dp[i] = min(m[i-1][0] + dp[i-1], m[i-2][1] + dp[i-2])

    res = dp[-1]
    dp2 = dp[:]

    for i in range(0, n-3):
        if dp[i] + k < dp[i+3]:
            dp2[i+3] = dp[i] + k
            for j in range(i+4, n):
                dp2[j] = min(dp[j], dp2[j-1] + m[j-1][0], dp2[j-2] + m[j-2][1])
            res = min(res, dp2[-1])

    return res

n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n-1)]
k = int(input())

print(min_energy(n, m, k))