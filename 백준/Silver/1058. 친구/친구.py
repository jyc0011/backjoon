import sys
input = sys.stdin.readline

N = int(input().strip())
graph = [list(input().strip()) for _ in range(N)]

ans = 0

for i in range(N):
    friends = set()
    for j in range(N):
        if graph[i][j] == 'Y':
            friends.add(j)
    for friend in list(friends):
        for k in range(N):
            if graph[friend][k] == 'Y' and k != i:
                friends.add(k)
    
    ans = max(ans, len(friends))

print(ans)