import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited, field):
    queue = deque([(x, y)])
    visited[x][y] = True
    color = field[x][y]
    connected = [(x, y)]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and field[nx][ny] == color:
                queue.append((nx, ny))
                visited[nx][ny] = True
                connected.append((nx, ny))
    if len(connected) >= 4:
        for x, y in connected:
            field[x][y] = '.'
        return True
    return False

def gravity(field):
    for y in range(6):
        stack = []
        for x in range(12):
            if field[x][y] != '.':
                stack.append(field[x][y])
        for x in range(11, -1, -1):
            if stack:
                field[x][y] = stack.pop()
            else:
                field[x][y] = '.'

field=[list(sys.stdin.readline().rstrip()) for _ in range(12)]
cnt=0

while True:
    visited = [[False] * 6 for _ in range(12)]
    chain = False
    for x in range(12):
        for y in range(6):
            if field[x][y] != '.' and not visited[x][y]:
                if bfs(x, y, visited, field):
                    chain = True
    if chain:
        cnt += 1
        gravity(field)
    else:
        break

print(cnt)