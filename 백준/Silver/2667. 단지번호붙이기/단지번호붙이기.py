import sys

N = int(sys.stdin.readline())
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

# DFS
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        count += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
result.sort()
for r in result:
    print(r)