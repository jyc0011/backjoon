import sys
from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread_virus(walls):
    q = deque(virus)
    # 바이러스가 퍼진 위치를 추적
    spread = set()
    while q:
        vx, vy = q.popleft()
        for dir in range(4):
            nx, ny = vx + dx[dir], vy + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                q.append((nx, ny))
                spread.add((nx, ny))  # 바이러스가 퍼진 위치 기록

    safe_count = len(empty) - len(spread) - 3  # 안전한 영역 계산 (-3은 벽을 세운 3칸 제외)

    # 퍼진 바이러스와 세웠던 벽을 원래대로 복구
    for vx, vy in spread:
        lab[vx][vy] = 0
    for wx, wy in walls:
        lab[wx][wy] = 0

    return safe_count


# 입력 받기
n, m = map(int, sys.stdin.readline().rstrip().split())
lab = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

empty, virus = [], []

# 벽과 바이러스 위치 탐색
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

ans = 0
for walls in combinations(empty, 3):
    # 벽 설치
    for wx, wy in walls:
        lab[wx][wy] = 1

    # 바이러스 확산 후 안전 지역 계산
    ans = max(ans, spread_virus(walls))

print(ans)