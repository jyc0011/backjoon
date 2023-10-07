import sys
from collections import deque
import copy

input = sys.stdin.readline

dx = [0, -1, 0]
dy = [-1, 0, 1]

def calc_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_enemy(col,board):
    queue = deque()
    queue.append([N-1, col])
    while queue:
        x, y = queue.popleft()
        if calc_distance(N, x, col, y) > D:
            return False
        if board[x][y] == 1:
            return (x, y)
        for i in range(3):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < N and 0 <= ay < M:
                queue.append([ax, ay])

def move_enemy(board):
    for j in range(M):
        for i in range(N-2, -1, -1):
            board[i+1][j] = board[i][j]
    for i in range(M):
        board[0][i] = 0

def del_enemy(board):
    cnt = 0
    for i in range(M):
        if board[N-1][i] == 1:
            cnt += 1
    return cnt

N, M, D = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
cnt_enemy = sum(row.count(1) for row in maps)
answer = 0

def run_simulation(archer_positions):
    global answer
    del_cnt = 0
    curr_enemy = cnt_enemy
    board = copy.deepcopy(maps)

    while curr_enemy > 0:
        tmp = set()
        for i in archer_positions:
            enemy_pos = find_enemy(i,board)
            if enemy_pos:
                tmp.add(enemy_pos)
        for x, y in tmp:
            board[x][y] = 0
        del_cnt += len(tmp)
        curr_enemy -= len(tmp)
        curr_enemy -= del_enemy(board)
        move_enemy(board)
    answer = max(answer, del_cnt)

for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            run_simulation([i, j, k])

print(answer)