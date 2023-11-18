def dfs(start, end, remaining_cost, max_shame, visited, board, answer):
    if start == end:
        return min(answer, max_shame)

    visited[start] = True
    local_answer = answer

    for next_node, next_cost in board[start]:
        if not visited[next_node] and next_cost <= remaining_cost:
            local_answer = min(local_answer, dfs(next_node, end, remaining_cost - next_cost, max(max_shame, next_cost), visited, board, local_answer))

    visited[start] = False
    return local_answer

n, m, a, b, c = map(int, input().split())
board = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    n1, n2, cost = map(int, input().split())
    board[n1].append((n2, cost))
    board[n2].append((n1, cost))

answer = dfs(a, b, c, 0, visited, board, float('inf'))

print(answer if answer != float('inf') else -1)