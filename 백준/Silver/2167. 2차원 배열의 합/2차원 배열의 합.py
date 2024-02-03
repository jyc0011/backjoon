N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

p = [[0 for i in range(0, M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        p[i][j] = (p[i][j-1] + p[i-1][j] 
                            - p[i-1][j-1] + A[i-1][j-1])

Q = int(input())

for _ in range(Q):
    i, j, x, y = map(int, input().split())
    print(p[x][y] - p[x][j-1] - p[i-1][y] + p[i-1][j-1])