import sys
from collections import deque

def dfs(v):
    visited[v] = True  # 현재 노드를 방문 처리
    print(v, end=' ')  # 방문 노드 출력
    for i in sorted(graph[v]):  # 정점 번호가 작은 것부터 방문
        if not visited[i]:  # 방문하지 않았다면
            dfs(i)  # 재귀적으로 방문

def bfs(v):
    queue = deque([v])  # 시작 정점을 큐에 삽입
    visited[v] = True  # 시작 정점을 방문 처리
    while queue:
        v = queue.popleft()  # 큐에서 하나의 정점을 뽑아 출력
        print(v, end=' ')
        for i in sorted(graph[v]):  # 정점 번호가 작은 것부터 방문
            if not visited[i]:  # 방문하지 않았다면
                queue.append(i)  # 큐에 삽입
                visited[i] = True  # 방문 처리

n,m,v=map(int, sys.stdin.readline().rstrip().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dfs(v)
print()

visited = [False] * (n + 1)
bfs(v)