from collections import deque

def bfs(start, graph, n, visited):
    queue = deque([start])
    visited[start] = True
    count = 1
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

def solution(n, wires):
    min_diff = float('inf')
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        visited = [False] * (n + 1)
        count = bfs(a, graph, n, visited)
        diff = abs(n - 2 * count)
        min_diff = min(min_diff, diff)
        graph[a].append(b)
        graph[b].append(a)

    return min_diff
