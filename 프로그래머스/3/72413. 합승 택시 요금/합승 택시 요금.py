import heapq

def dijkstra(n, s, graph):
    dist = [float('inf')] * (n + 1) # 초기화
    dist[s] = 0
    queue = []
    heapq.heappush(queue, (0, s))
    
    while queue:
        now_dist, now_node = heapq.heappop(queue) # 가까운 노드 선택
        if dist[now_node] < now_dist: # 이미 했으면 건너뜀
            continue
        for adj, w in graph[now_node].items(): # 인접 노드 탐색
            cost = now_dist + w # 비용 계산
            if cost < dist[adj]: # 더 저렴하면
                dist[adj] = cost # 갱신
                heapq.heappush(queue, (cost, adj))
    return dist # 모든 노드까지의 최단 거리 반환

def solution(n, s, a, b, fares):
    graph = [{} for _ in range(n + 1)] # 노드 간의 거리 저장
    for c, d, f in fares: # 주어진 정보를 정리
        graph[c][d] = f # 양 방향 이동 가능
        graph[d][c] = f
    min_cost = float('inf') # 초기화
    for i in range(1, n + 1): # 다익스트라 실행
        dist = dijkstra(n, i, graph) # 다른 노드까지의 최단 거리 계산
        total_cost = dijkstra(n, s, graph)[i] + dist[a] + dist[b] # 합승했다 헤어지는 비용
        min_cost = min(min_cost, total_cost) # 최소 비용 찾기
    return min_cost