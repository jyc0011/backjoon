import sys
input = sys.stdin.readline

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(T):
    cmd = input().strip()
    x = y = 0
    dir = 0
    min_x = max_x = 0
    min_y = max_y = 0
    for c in cmd:
        if c == 'F':
            x += dx[dir]
            y += dy[dir]
        elif c == 'B':
            x -= dx[dir]
            y -= dy[dir]
        elif c == 'L':
            dir = (dir + 3) % 4
        elif c == 'R':
            dir = (dir + 1) % 4
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    width = max_x - min_x
    height = max_y - min_y
    print(width * height)