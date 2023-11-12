import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(graph, start, V):
    distances = [INF] * (V + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adj, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(queue, (distance, adj))

    return distances

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distances = dijkstra(graph, K, V)

for i in range(1, V + 1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])
