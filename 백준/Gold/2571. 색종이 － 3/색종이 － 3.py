import sys

input=sys.stdin.readline

arr = [[0] * 100 for _ in range(100)]
N = int(input())

for _ in range(N):
    start_x, start_y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[start_x+i][start_y+j] = 1
            
for x in range(100):
    for y in range(100):
        if arr[x][y] and x > 0:
            arr[x][y] += arr[x-1][y]
ans = 0

for x in range(100):
    for y in range(100):
        min_height = 100
        for z in range(y, 100):
            min_height = min(min_height, arr[x][z])
            ans = max(ans, min_height * (z - y + 1))

print(ans)