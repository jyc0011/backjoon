import sys
from collections import deque

input = sys.stdin.readline
LIMIT = {'0', '2', '3', '4', '5'}

n, m = map(int, input().split())
grid = []
sr = sc = -1

for r in range(n):
    row = input().strip()
    grid.append(row)
    if '2' in row:
        sr, sc = r, row.index('2')

dq = deque([(sr, sc)])
visited = [bytearray(m) for _ in range(n)]
visited[sr][sc] = 1
time = 0

while dq:
    for _ in range(len(dq)):
        r, c = dq.popleft()
        cell = grid[r][c]
        if cell in '345':
            print("TAK")
            print(time)
            sys.exit(0)
        if r > 0 and not visited[r-1][c] and grid[r-1][c] in LIMIT:
            visited[r-1][c] = 1
            dq.append((r-1, c))
        if r+1 < n and not visited[r+1][c] and grid[r+1][c] in LIMIT:
            visited[r+1][c] = 1
            dq.append((r+1, c))
        if c > 0 and not visited[r][c-1] and grid[r][c-1] in LIMIT:
            visited[r][c-1] = 1
            dq.append((r, c-1))
        if c+1 < m and not visited[r][c+1] and grid[r][c+1] in LIMIT:
            visited[r][c+1] = 1
            dq.append((r, c+1))
    time += 1
print("NIE")