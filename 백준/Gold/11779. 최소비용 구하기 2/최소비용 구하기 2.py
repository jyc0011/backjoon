import sys
import heapq

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
A, B = map(int, input().split())
INF = float('inf')
dist = [INF] * (n+1)
prev = [0] * (n+1)
dist[A] = 0
hq = []
heapq.heappush(hq, (0, A))
while hq:
    cost, cur = heapq.heappop(hq)
    if cost > dist[cur]:
        continue
    for nxt, w in graph[cur]:
        if dist[nxt] > cost + w:
            dist[nxt] = cost + w
            prev[nxt] = cur
            heapq.heappush(hq, (dist[nxt], nxt))
print(dist[B])
path = []
cur = B
while cur != 0:
    path.append(cur)
    cur = prev[cur]
path.reverse()
print(len(path))
print(" ".join(map(str, path)))