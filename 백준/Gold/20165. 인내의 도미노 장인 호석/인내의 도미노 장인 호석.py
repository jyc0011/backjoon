import sys

# 방향 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dir_map = {"E": 0, "W": 1, "S": 2, "N": 3}

def attack(x, y, d):
    global state, height, attack_point
    # 이미 넘어진 도미노이면 아무일도 일어나지 않음
    if state[x][y] == "F":
        return
    count = height[x][y]  # 첫번째 도미노 높이
    while count:
        # 영역을 벗어났는지 확인
        if not 0 <= x < n or not 0 <= y < m:
            break
        # 현재 도미노가 서있으면 넘어뜨림
        if state[x][y] == "S":
            state[x][y] = "F"
            attack_point += 1
            count = max(count, height[x][y])  # 지금 넘어뜨린 도미노들 중 가장 높은 걸로 업데이트
        # 그 방향으로 이동
        x += dx[d]
        y += dy[d]
        count -= 1  # 쓰러진 도미노만큼 감소

def defence(x, y):
    global state
    state[x][y] = "S"

n, m, r = map(int, sys.stdin.readline().rstrip().split())
height = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
state = [["S" for _ in range(m)] for _ in range(n)]
attack_point = 0

for _ in range(r):
    x, y, d = sys.stdin.readline().rstrip().split()
    attack(int(x)-1, int(y)-1, dir_map[d])
    x, y = map(int, sys.stdin.readline().rstrip().split())
    defence(x-1, y-1)
    
print(attack_point)
for row in state:
    print(' '.join(row))