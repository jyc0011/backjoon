import sys

# 방향
d = [[0, -1], [0, 1], [1, 0], [-1, 0]]

# 왼쪽으로 움직일 때 모래 미는 정도
s_l = [(1, 1, 0.01), (-1, 1, 0.01),
       (1, 0, 0.07), (-1, 0, 0.07),
       (1, -1, 0.1), (-1, -1, 0.1),
       (2, 0, 0.02), (-2, 0, 0.02),
       (0, -2, 0.05), (0, -1, 0)]

# 오른쪽으로 움직일 때 모래 미는 정도
s_r = [(x, -y, z) for x, y, z in s_l]

# 아래쪽으로 움직일 때 모래 미는 정도
s_d = [(-y, x, z) for x, y, z in s_l]

# 위쪽으로 움직일 때 모래 미는 정도
s_u = [(y, x, z) for x, y, z in s_l]

# 토네이도 함수
def tornado(block, dx, dy, direction):
    global ans, s_x, s_y, sand

    for _ in range(block):
        s_x += dx
        s_y += dy
        if s_y < 0:
            break

        total = 0

        for dx, dy, z in direction:
            nx = s_x + dx
            ny = s_y + dy

            if z == 0:
                new_sand = sand[s_x][s_y] - total
            else:
                new_sand = int(sand[s_x][s_y] * z)
                total += new_sand

            if 0 <= nx < N and 0 <= ny < N: # 격자 내부에 퍼진 모래
                sand[nx][ny] += new_sand
            else: # 격자 밖으로 나간 모래
                ans += new_sand

N = int(sys.stdin.readline())
sand = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 토네이도 시작 위치
s_x, s_y = N // 2, N // 2

ans = 0

# 토네이도 이동 및 모래 이동
for i in range(1, N+1):
    if i % 2 == 1: # 움직이는 칸 수가 홀수인 경우
        tornado(i, d[0][0], d[0][1], s_l)
        tornado(i, d[2][0], d[2][1], s_d)
    else: # 움직이는 칸 수가 짝수인 경우
        tornado(i, d[1][0], d[1][1], s_r)
        tornado(i, d[3][0], d[3][1], s_u)

print(ans)