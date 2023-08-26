import heapq
import sys

def dijkstra(graph, start):
    # 각 노드까지의 최단 거리를 저장할 리스트 초기화
    distances = [float('infinity') for _ in graph]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])  # 시작 노드와 거리를 큐에 삽입

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # 현재 노드까지의 기록된 거리보다 큐에서 뽑은 거리가 크다면 이미 더 짧은 경로를 찾은 것이므로 무시
        if distances[current_node] < current_distance:
            continue
        
        # 현재 노드의 인접한 노드와 그 노드까지의 거리를 순회
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight  # 현재 노드를 거쳐 가는 거리
            # 새로운 경로가 더 짧다면 최단 거리를 갱신
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])  # 새로운 거리와 노드를 큐에 삽입
                
    return distances  # 최단 거리 리스트 반환

# 입력 받기
n = int(sys.stdin.readline())
a, b, c = map(int, sys.stdin.readline().split())

# 그래프 초기화: 각 노드마다 인접한 노드와 그 노드까지의 거리를 저장
graph = [[] for _ in range(n+1)]
m = int(sys.stdin.readline())

# 도로 정보 입력 받기
for _ in range(m):
    d, e, l = map(int, sys.stdin.readline().split())
    graph[d].append([e, l])
    graph[e].append([d, l])

# 각 친구의 집에서 모든 땅까지의 최단 거리 계산
distances_a = dijkstra(graph, a)
distances_b = dijkstra(graph, b)
distances_c = dijkstra(graph, c)

max_distance = -1
result = 0

# 모든 땅을 순회하면서 각 친구의 집까지의 최단 거리 중 가장 짧은 거리가 가장 긴 땅을 찾음
for i in range(1, n+1):
    current_min_distance = min(distances_a[i], distances_b[i], distances_c[i])
    if current_min_distance > max_distance:
        max_distance = current_min_distance
        result = i

print(result)  # 결과 출력