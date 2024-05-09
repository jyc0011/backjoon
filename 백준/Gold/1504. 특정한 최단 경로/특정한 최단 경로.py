import heapq
import sys

input=sys.stdin.readline

def dijkstra(start, adj, N):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        if current_dist > dist[current_node]:
            continue
        for next_node, weight in adj[current_node]:
            new_dist = current_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(queue, (new_dist, next_node))
    return dist

N,E=map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(E):
    a,b,c=map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

v1,v2=map(int, input().split())

dist1 = dijkstra(1, adj, N)
dist_v1 = dijkstra(v1, adj, N)
dist_v2 = dijkstra(v2, adj, N)

route1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
route2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

answer = min(route1, route2)

if answer >= float('inf'):
    print(-1)
else:
    print(answer)