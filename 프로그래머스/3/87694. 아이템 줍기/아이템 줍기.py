from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 102
    board = [[0] * N for _ in range(N)]
    for rec in rectangle:
        x1, y1, x2, y2 = [v * 2 for v in rec]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1
    for rec in rectangle:
        x1, y1, x2, y2 = [v * 2 for v in rec]
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0
    sx, sy = characterX * 2, characterY * 2
    ex, ey = itemX * 2, itemY * 2
    q = deque()
    q.append((sx, sy, 0))
    visit = [[False] * N for _ in range(N)]
    visit[sx][sy] = True
    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
        pass

    while q:
        x, y, d = q.popleft()
        if (x, y) == (ex, ey):
            return d // 2
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and board[nx][ny]:
                visit[nx][ny] = True
                q.append((nx, ny, d + 1))
    return 0