import sys

input = sys.stdin.readline
INF = float('inf')

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    fly_info = [list(map(int, input().split())) for _ in range(K)]
    
    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    dp[1][0] = 0
    
    for cost in range(M + 1):
        for u, v, c, d in fly_info:
            if cost + c <= M and dp[u][cost] + d < dp[v][cost + c]:
                dp[v][cost + c] = dp[u][cost] + d
    
    answer = min(dp[N])
    if answer == INF:
        print("Poor KCM")
    else:
        print(answer)