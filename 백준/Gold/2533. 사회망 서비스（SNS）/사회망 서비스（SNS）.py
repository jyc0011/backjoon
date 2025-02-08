import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(u, parent):
    dp[u][0] = 0
    dp[u][1] = 1
    for v in graph[u]:
        if v == parent:
            continue
        dfs(v, u)
        dp[u][0] += dp[v][1]
        dp[u][1] += min(dp[v][0], dp[v][1])

N = int(input().strip())
global graph, dp
graph = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(1, -1)
print(min(dp[1][0], dp[1][1]))