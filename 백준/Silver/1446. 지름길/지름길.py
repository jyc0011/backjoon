import heapq

def dijkstra(start):
    distance = [float('inf')] * (D + 1)
    distance[start] = 0
    queue = [(0, start)]
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for next_node, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
    return distance

N, D = map(int, input().split())
graph = [[] for _ in range(D + 1)]

for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    start, end, length = map(int, input().split())
    if end <= D:
        graph[start].append((end, length))

distance = dijkstra(0)
print(distance[D])