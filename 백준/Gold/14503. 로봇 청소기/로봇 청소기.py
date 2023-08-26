import sys
# 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고
    # 처음으로
    # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동 중지
# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    # 반시계 방향으로 90도 회전
    # 바라보는 방향 기준으로 앞쪽 칸이 청소X 빈 칸
    # 힌 칸 전진
    # 처음으로 돌아감

# 북, 동, 남, 서 방향에 대한 변화량
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def clean_room(x, y, d):
    count = 0  # 청소한 칸의 개수
    
    while True:
        if room[x][y] == 0:  # 현재 칸이 청소되지 않은 경우
            room[x][y] = 2  # 현재 칸 청소 표시
            count += 1
        
        can_clean = False  # 주변에 청소할 수 있는 칸이 있는지 체크
        for i in range(4):
            d = (d - 1) % 4  # 왼쪽(반시계) 방향으로 회전
            nx, ny = x + dx[d], y + dy[d]  # 새로운 좌표 계산
            
            if room[nx][ny] == 0:  # 청소하지 않은 칸인 경우
                x, y = nx, ny  # 전진
                can_clean = True  # 청소할 수 있는 칸이 있음을 표시
                break
        
        # 청소할 칸이 없을 때
        if not can_clean:
            nx, ny = x - dx[d], y - dy[d]  # 후진할 좌표 계산
            if room[nx][ny] == 1:  # 만약 뒤가 벽인 경우
                break
            x, y = nx, ny  # 후진

    return count

print(clean_room(r, c, d))  # 청소한 칸의 개수 출력