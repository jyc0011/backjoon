def flood_fill():
    check[i][j] = val
    q.append((i,j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] and not check[nx][ny]:
                    check[nx][ny] = val
                    q.append((nx, ny))

from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

t = int(input())
for ___ in range(t):
    m, n, k = map(int,input().split())
    arr = [[0]*m for _ in range(n)]
    for i in range(k):
        y, x = map(int,input().split())
        arr[x][y] = 1
    check = [[0]*m for _ in range(n)]
    val = 1

    q = deque()
    for i in range(n):
        for j in range(m):
            if check[i][j] == 0 and arr[i][j] == 1:
                flood_fill()
                val += 1
    print(val - 1)