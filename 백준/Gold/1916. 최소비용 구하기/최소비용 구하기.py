import heapq
import sys

# 다익스트라
def dijkstra(start, adj, N):
    dist = [float('inf')] * (N + 1)  # 거리를 무한대로 초기화
    dist[start] = 0  # 시작 도시의 거리 0
    queue = [(0, start)]  # 우선순위 큐 초기화

    while queue:
        current_dist, current_node = heapq.heappop(queue)  # 현재 노드와 거리를 큐에서 꺼냄
        if dist[current_node] < current_dist: # 현재 노드까지의 거리가 이미 짧으면 
            continue  # 무시

        for next_node, weight in adj[current_node]: # 현재 노드에 인접한 노드에서
            new_dist = current_dist + weight  # 새로운 거리 계산
            if new_dist < dist[next_node]:  # 기존 거리보다 짧은 경우 업데이트
                dist[next_node] = new_dist
                heapq.heappush(queue, (new_dist, next_node))  # 업데이트된 거리를 큐에 추가
    return dist

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수
adj = [[] for _ in range(N + 1)]  # 인접 리스트 초기화

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())  # 버스 정보 입력 받음
    adj[u].append((v, w))  # 인접 리스트에 버스 정보 추가

A, B = map(int, sys.stdin.readline().rstrip().split())  # 출발 도시와 도착 도시
print(dijkstra(A, adj, N)[B])  # 결과 출력