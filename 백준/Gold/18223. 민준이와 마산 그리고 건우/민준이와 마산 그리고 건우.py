import heapq
import sys

input = sys.stdin.readline
def dijkstra(start):
    dist = [float('inf')] * V
    dist[start] = 0
    min_heap = [(0, start)]
    while min_heap:
        current_dist, u = heapq.heappop(min_heap)
        if current_dist > dist[u]:
            continue
        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(min_heap, (dist[v], v))
    return dist

V,E,P=map(int, input().rstrip().split())
P -= 1

adj = [[] for _ in range(V)]
for _ in range(E):
    a,b,c=map(int, input().rstrip().split())
    a -= 1
    b -= 1
    adj[a].append((b, c))
    adj[b].append((a, c))

dist_from_1 = dijkstra(0)
dist_from_P = dijkstra(P)

if dist_from_1[P] + dist_from_P[V - 1] == dist_from_1[V - 1]:
    print("SAVE HIM")
else:
    print("GOOD BYE")