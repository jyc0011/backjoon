from collections import deque
import sys

def bfs(x, y, f):
    q = deque([(x, y)])
    c = f[x][y]
    f[x][y] = '*'
    count = 1
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 12 and 0 <= ny < 6 and f[nx][ny] == c:
                q.append((nx, ny))
                f[nx][ny] = '*'
                count += 1
    
    if count >= 4:
        for x in range(12):
            for y in range(6):
                if f[x][y] == '*':
                    f[x][y] = '.'
        return True
    else:
        for x in range(12):
            for y in range(6):
                if f[x][y] == '*':
                    f[x][y] = c
        return False

def gravity(f):
    for y in range(6):
        bottom = 11
        for x in range(11, -1, -1):
            if f[x][y] != '.':
                if x != bottom:
                    f[bottom][y], f[x][y] = f[x][y], '.'
                bottom -= 1

f=[list(sys.stdin.readline().rstrip()) for _ in range(12)]
cnt = 0

while True:
    ch = False
    for x in range(12):
        for y in range(6):
            if f[x][y] not in ('.', '*'):
                if bfs(x, y, f):
                    ch = True
    if ch:
        cnt += 1
        gravity(f)
    else:
        break

print(cnt)
