import heapq
import sys

# 1--3-4
# s1 | s2
#    2
#    t

# 플레이어들이 각자 수도로 오는게 아니라
# 역으로 수도에서 출발해서 도시로 가게 시킴
# -> 중복해서 길 못지나간다는 조건 고려할 필요가 없어짐
# 거꾸로 가서 먼저 도착 -> 먼저 도착한 플레이어 승자
# 동시 도착 -> 플레이어 1의 무조건 승

# 다익스트라
def dijkstra(s): 
    # 거리 리스트 무한대로 초기화
    distances = [float('inf') for _ in range(N+1)]
    # 우선순위 큐 -> 최단거리 찾기
    hq = []
    # 시작 점은 0
    heapq.heappush(hq, (0, s))
    distances[s] = 0 

    while hq: # 모든 노드에 대해 순회
        dist, now = heapq.heappop(hq)
        if distances[now] < dist: # 거리가 이미 더 짧음
            continue # 무시
        for i in road[now]: # 인접 노드 순회
            next_node = i[0]
            cost = dist + i[1]
            if cost < distances[next_node]: # 새로 계산한게 기존보다 짧음
                distances[next_node] = cost # 갱신
                heapq.heappush(hq, (cost, next_node)) # 추가
    return distances

# 도시, 거리
N, M = map(int,sys.stdin.readline().rstrip().split())
# 도시의 연결 상태&거리 저장
road = [[] for _ in range(N+1)]

for _ in range(M):
    # 도시1, 도시2, 마을갯수
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    road[a].append((b,c)) # 도로 양 쪽으로 다 갈 수 있음
    road[b].append((a,c))

# road =[[(3, 2)], [(3, 3)], [(1, 2), (2, 3), (4, 1)], [(3, 1)]]

# s1 플1 s2 플2 t 수도
s1, s2, t = map(int,sys.stdin.readline().rstrip().split())
 
distances= dijkstra(t)

if distances[s1]<=distances[s2]:
    print("First")
else:
    print("Second")