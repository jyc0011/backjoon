import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N
INF = 2147000000
min_diff = INF

def DFS(team_size, idx):
    global min_diff
    if team_size == N // 2:
        sum_team_A = 0
        sum_team_B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    sum_team_A += board[i][j]
                elif not visited[i] and not visited[j]:
                    sum_team_B += board[i][j]
        min_diff = min(min_diff, abs(sum_team_A - sum_team_B))
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(team_size + 1, i + 1)
            visited[i] = False

half_N = N // 2
for start in range(N - half_N + 1):
    visited[start] = True
    DFS(1, start + 1)
    visited[start] = False

print(min_diff)
