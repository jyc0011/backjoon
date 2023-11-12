import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for r in range(n):
    for c in range(n):
        if r == 0 and c == 0:
            continue

        cost_from_top = int(1e7) if r == 0 else dp[r-1][c] + max(0, arr[r][c] - arr[r-1][c] + 1)
        cost_from_left = int(1e7) if c == 0 else dp[r][c-1] + max(0, arr[r][c] - arr[r][c-1] + 1)

        dp[r][c] = min(cost_from_top, cost_from_left)

print(dp[n-1][n-1])