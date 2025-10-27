import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000 + 10)
MAX_SUM = 200000

def calc(val, isP):
    return a if isP[val] else b

N, a, b = map(int, input().split())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
isP = [True] * (MAX_SUM + 1)
isP[0] = isP[1] = False

for i in range(2, int(MAX_SUM**0.5) + 1):
    if isP[i]:
        for j in range(i * i, MAX_SUM + 1, i):
            isP[j] = False

dp = [0] * (N + 1)

if N >= 1:
    dp[1] = calc(row1[0] + row2[0], isP)

for i in range(2, N + 1):
    score_vertical = dp[i-1] + calc(row1[i-1] + row2[i-1],isP)
    score_horizontal = dp[i-2] + calc(row1[i-2] + row1[i-1],isP) + calc(row2[i-2] + row2[i-1],isP)
    dp[i] = max(score_vertical, score_horizontal)

print(dp[N])