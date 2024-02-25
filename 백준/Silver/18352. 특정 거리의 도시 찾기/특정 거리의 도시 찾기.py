import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node in graph[now]:
            cost = dist + 1
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
distance = [float('inf')] * (N + 1)
dijkstra(X)
check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if not check:
    print(-1)