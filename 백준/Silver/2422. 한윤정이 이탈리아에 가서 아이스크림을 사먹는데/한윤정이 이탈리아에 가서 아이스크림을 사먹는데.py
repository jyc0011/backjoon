import sys

input=sys.stdin.readline

n,m=map(int, input().split())

no=[[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    no[x][y] = True
    no[y][x] = True
    
cnt=0

for i in range(1, n-1):
    for j in range(i+1, n):
        if no[i][j]:
            continue
        for k in range(j+1, n+1):
            if no[i][k] or no[j][k]:
                continue
            cnt += 1

print(cnt)