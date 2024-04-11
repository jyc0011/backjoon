import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(building, keys, h, w):
    queue = deque()
    doors = [[] for _ in range(26)]  # 문 대기열
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    ans = 0
    new_building = ['.' * (w + 2)] + ['.' + row + '.' for row in building] + ['.' * (w + 2)]
    h += 2
    w += 2

    # 빌딩의 가장자리 위치 큐에 추가
    for i in range(h):
        queue.append((i, 0))
        queue.append((i, w - 1))
        visited[i][0] = visited[i][w - 1] = True
    for j in range(w):
        queue.append((0, j))
        queue.append((h - 1, j))
        visited[0][j] = visited[h - 1][j] = True

    while queue:
        x, y = queue.popleft()
        if new_building[x][y] == '$':
            ans += 1
        elif 'a' <= new_building[x][y] <= 'z':
            key_index = ord(new_building[x][y]) - ord('a')
            if not keys[key_index]:  # 새로운 열쇠를 발견한 경우
                keys[key_index] = True
                queue.extend(doors[key_index])  # 해당 문의 대기열을 큐에 추가
                doors[key_index] = []  # 대기열 비우기
        elif 'A' <= new_building[x][y] <= 'Z':
            door_index = ord(new_building[x][y]) - ord('A')
            if keys[door_index]:  # 열쇠가 있는 경우
                pass  # 문을 열고 계속 진행
            else:
                doors[door_index].append((x, y))  # 문 대기열에 추가
                continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and new_building[nx][ny] != '*':
                visited[nx][ny] = True
                queue.append((nx, ny))
    return ans

T = int(input().strip())

for _ in range(T):
    h, w = map(int, input().rstrip().split())
    building = [input().rstrip() for _ in range(h)]
    key_input = input().rstrip()
    keys = [False] * 26
    if key_input != '0':
        for k in key_input:
            keys[ord(k) - ord('a')] = True
    print(bfs(building, keys, h, w))