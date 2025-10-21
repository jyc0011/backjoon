import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
val = {'R': 0, 'S': 1, 'P': 2}
dp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for char in S:
    v = val[char]
    prev_v = (v + 2) % 3
    for i in range(3):
        new_len = 0
        if v == i:
            new_len = 1
        if dp[i][prev_v] > 0:
            new_len = max(new_len, dp[i][prev_v] + 1)
        if new_len > 0:
            dp[i][v] = max(dp[i][v], new_len)

K_max = max(dp[0][2], dp[1][0], dp[2][1])
print(N - K_max)