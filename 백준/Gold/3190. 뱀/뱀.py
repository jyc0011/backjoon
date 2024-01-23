import sys

def move(snake, direction, board):
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)
    if (new_head[0] < 0 or new_head[0] >= len(board) or new_head[1] < 0 or new_head[1] >= len(board[0]) or new_head in snake):
        return False
    if board[new_head[0]][new_head[1]] == 1:
        eat(snake, new_head, board)
    else:
        snake.pop()
        snake.insert(0, new_head)
    return True

def eat(snake, new_head, board):
    board[new_head[0]][new_head[1]] = 0
    snake.insert(0, new_head)

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    board[x-1][y-1] = 1

l = int(input())
m = [sys.stdin.readline().rstrip().split() for _ in range(l)]
for i in range(l):
    m[i][0] = int(m[i][0])

snake = [(0, 0)]
now_dir = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
time = 0
m_idx = 0

while True:
    time += 1
    if not move(snake, directions[now_dir], board):
        break
    if m_idx < len(m) and time == m[m_idx][0]:
        if m[m_idx][1] == 'L':
            now_dir = (now_dir - 1) % 4
        else:  # 'D'
            now_dir = (now_dir + 1) % 4
        m_idx += 1

print(time)