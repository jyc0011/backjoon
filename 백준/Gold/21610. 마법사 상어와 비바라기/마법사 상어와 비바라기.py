import sys

d8 = [[0,0], [0, -1], [-1,-1], [-1, 0], [-1,1],
      [0, 1], [1,1], [1, 0], [1,-1]]
d4 = [[-1,-1], [-1,1], [1,1], [1,-1]]

def move(dx, dy, s, cloud, N, A):
    now_cloud = [( (y + dy * s) % N, (x + dx * s) % N) for y, x in cloud]
    for y, x in now_cloud:
        A[y][x] += 1
    water(now_cloud, A, N)
    return rain(now_cloud, A, N)

def water(now_cloud, A, N):
    for y, x in now_cloud:
        cnt = sum(1 for dy, dx in d4
                  if 0 <= y + dy < N and 0 <= x + dx < N and A[y+dy][x+dx] > 0)
        A[y][x] += cnt

def rain(now_cloud, A, N):
    now_cloud_set = set(now_cloud)
    new_cloud = [(y, x) for y in range(N) for x in range(N) if (y, x) not in now_cloud_set and A[y][x] >= 2]
    for y, x in new_cloud:
        A[y][x] -= 2
    return new_cloud

N ,M = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
cloud = [(N-2,0), (N-2,1), (N-1,0), (N-1,1)]

for _ in range(M):
    d,s=map(int, sys.stdin.readline().rstrip().split())
    cloud = move(d8[d][1], d8[d][0], s, cloud, N, A)

print(sum(sum(row) for row in A))