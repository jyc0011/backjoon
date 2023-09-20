import sys
d8 =[[0,0],[0, -1],[-1,-1],[-1, 0],[-1,1],[0, 1],[1,1],[1, 0],[1,-1]]
d4=[[-1,-1],[-1,1],[1,1],[1,-1]]

def move(dx, dy, s):
    global cloud, N, A
    now_cloud = []
    for y, x in cloud:
        ny = (y + dy * s) % N
        nx = (x + dx * s) % N
        A[ny][nx] += 1
        now_cloud.append((ny, nx))
    water(now_cloud)
    rain(now_cloud)


def water(now_cloud):
    global A, d4
    for y, x in now_cloud:
        cnt = 0
        for d in range(4):
            ny = y + d4[d][0]
            nx = x + d4[d][1]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            elif A[ny][nx] > 0:
                cnt += 1
        A[y][x]+=cnt

def rain(now_cloud):
    new_cloud = []
    global cloud, N, A
    for y in range(N):
        for x in range(N):
            if (y,x) in now_cloud or A[y][x] < 2:
                continue
            A[y][x]-=2
            new_cloud.append((y, x))
    cloud = new_cloud

N ,M = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
cloud = [[N-2,0],[N-2,1],[N-1,0],[N-1,1]]

for _ in range(M):
    d,s=map(int, sys.stdin.readline().rstrip().split())
    move(d8[d][1], d8[d][0], s)

# 물의 양 합 계산 후 출력
result = 0
for y in range(N):
    for x in range(N):
        result += A[y][x]
print(result)