import sys

sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
LOG = 20

def dfs(x, depth, cost):# 루트 노드부터 깊이 및 거리 계산
    c[x] = True
    d[x] = depth
    dist[x] = cost  # 루트에서 현재 노드까지의 거리 저장
    for y, w in graph[x]:
        if not c[y]:  # 방문하지 않은 경우만 진행
            parent[y][0] = x
            dfs(y, depth + 1, cost + w)

def set_parent(): # 전체 부모 관계 및 거리 정보 설정
    dfs(1, 0, 0)  # 루트 노드는 1번, 거리 0으로 시작
    for i in range(1, LOG):
        for j in range(1, N + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

def lca(a, b):# 최소 공통 조상 찾기
    if d[a] > d[b]:  # 항상 b가 더 깊도록 조정
        a, b = b, a

    # 깊이 맞추기
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    # LCA 찾기
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

N = int(input())  # 노드 개수
parent = [[0] * LOG for _ in range(N + 1)]  # 부모 노드 정보
d = [0] * (N + 1)  # 각 노드의 깊이
c = [False] * (N + 1)  # 방문 여부
dist = [0] * (N + 1)  # 루트에서 현재 노드까지의 거리
graph = [[] for _ in range(N + 1)]  # 그래프 정보

for _ in range(N - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

set_parent()

M = int(input())  # 쿼리 개수
for _ in range(M):
    u, v = map(int, input().split())
    ancestor = lca(u, v)
    print(dist[u] + dist[v] - 2 * dist[ancestor])  # 거리 계산