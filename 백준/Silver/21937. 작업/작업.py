import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

x = int(input())

visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    count = 1
    for next_node in graph[node]:
        if not visited[next_node]:
            count += dfs(next_node)
    return count

print(dfs(x) - 1)