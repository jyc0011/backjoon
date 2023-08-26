import heapq
import sys

def dijkstra(graph, start):
    # 모든 노드까지의 거리를 무한대로 초기화
    distances = [float('infinity') for _ in graph]
    distances[start] = 0  # 시작 노드까지의 거리는 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 현재 노드의 인접한 노드들의 거리를 갱신
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances

# 입력 처리
N, V, E = map(int, input().split())
A, B = map(int, input().split())
homes = list(map(int, input().split()))

graph = [[] for _ in range(V+1)]

# 그래프 구성
for _ in range(E):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

total_distance = 0  # 전체 거리 합산을 위한 변수

# 각 집에서의 KIST와 씨알푸드까지의 거리 계산
for home in homes:
    distance_to_KIST = dijkstra(graph, home)[A]
    distance_to_CRFood = dijkstra(graph, home)[B]
    # 도달할 수 없는 경우 -1로 처리
    if distance_to_KIST == float('infinity'):
        distance_to_KIST = -1
    if distance_to_CRFood == float('infinity'):
        distance_to_CRFood = -1
    total_distance += (distance_to_KIST + distance_to_CRFood)

print(total_distance)  # 결과 출력
