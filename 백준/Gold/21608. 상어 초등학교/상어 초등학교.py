import sys
# 학생들을 순서대로 돌며 자리를 배치
# 각 학생에 대해
    # 교실의 모든 빈 자리에 대해 좋아하는 학생의 수를 확인
    # 좋아하는 학생의 수가 가장 많은 자리들 중에서
    # 인접한 빈 자리가 가장 많은 자리를 선택
    # 동점이 있는 경우에는 행과 열의 번호가 작은 것을 선택
# 모든 학생의 자리가 결정되면 만족도를 계산



N = int(sys.stdin.readline())

# 학생의 정보를 입력받음 (번호, 좋아하는 학생 4명)
students = [list(map(int, sys.stdin.readline().split())) for _ in range(N*N)]

# 교실을 0으로 초기화
room = [[0] * N for _ in range(N)]

# 상하좌우 움직임을 위한 변수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 주어진 좌표가 교실 내부에 있는지 확인하는 함수
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

# 학생의 자리를 찾는 함수
def find_seat(stu):
    max_like, max_empty, result = -1, -1, (-1, -1)
    for x in range(N):
        for y in range(N):
            # 빈 자리인 경우에만 체크
            if room[x][y] == 0:
                like_cnt, empty_cnt = 0, 0
                # 인접한 네 방향에 대해 좋아하는 학생의 수와 빈 칸의 수를 체크
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if is_valid(nx, ny):
                        if room[nx][ny] in stu[1:]:
                            like_cnt += 1
                        if room[nx][ny] == 0:
                            empty_cnt += 1
                # 최적의 자리를 업데이트
                if like_cnt > max_like or (like_cnt == max_like and empty_cnt > max_empty):
                    max_like, max_empty = like_cnt, empty_cnt
                    result = (x, y)
    return result

# 모든 학생에 대해 자리를 찾음
for stu in students:
    x, y = find_seat(stu)
    room[x][y] = stu[0]

# 만족도 계산 함수
def satisfaction(x, y, likes):
    cnt = 0
    # 인접한 네 방향에 대해 좋아하는 학생의 수를 체크
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if is_valid(nx, ny) and room[nx][ny] in likes:
            cnt += 1
    # 만족도를 반환
    if cnt == 1: return 1
    elif cnt == 2: return 10
    elif cnt == 3: return 100
    elif cnt == 4: return 1000
    else: return 0

# 전체 만족도를 계산
total = 0
for stu in students:
    x, y = -1, -1
    # 학생의 자리를 찾음
    for i in range(N):
        for j in range(N):
            if room[i][j] == stu[0]:
                x, y = i, j
                break
    # 만족도를 누적하여 합산
    total += satisfaction(x, y, stu[1:])

print(total)