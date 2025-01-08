import sys

N=int(input())
li=list(map(int, sys.stdin.readline().split()))
M=int(input())
num = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N - 1):
    if li[i] == li[i + 1]:
        dp[i][i + 1] = 1

for l in range(3, N + 1):
    for s in range(N - l + 1):
        e = s + l - 1
        if li[s] == li[e] and dp[s + 1][e - 1] == 1:
            dp[s][e] = 1

ans = [dp[S - 1][E - 1] for S, E in num]
sys.stdout.write("\n".join(map(str, ans)) + "\n")