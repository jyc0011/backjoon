import sys, heapq
input = sys.stdin.readline

INF = 10 ** 18
pq = [(0, 1, 0)]

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

INF = 10 ** 18
dist = [[INF] * (K + 1) for _ in range(N + 1)]
dist[1][0] = 0

while pq:
    time, u, p = heapq.heappop(pq)
    if time != dist[u][p]:
        continue
    if u == N:
        continue
    for v, w in graph[u]:
        nt = time + w
        if nt < dist[v][p]:
            dist[v][p] = nt
            heapq.heappush(pq, (nt, v, p))
        if p < K and time < dist[v][p + 1]:
            dist[v][p + 1] = time
            heapq.heappush(pq, (time, v, p + 1))
print(min(dist[N]))