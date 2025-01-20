import sys
from collections import deque

input = sys.stdin.readline
D = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),( 1, -1), (1, 0), (1, 1)]
ans = 10**9
l,r = 0,0

def calc(lo, h):
    if not (lo <= height[px][py] <= h):
        return False

    visited = [[False]*n for _ in range(n)]
    q = deque([(px, py)])
    visited[px][py] = True
    cnt = 0

    while q:
        x, y = q.popleft()
        if G[x][y] == 'K':
            cnt += 1
            if cnt == kCnt:
                return True

        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if lo <= height[nx][ny] <= h:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return False

n = int(input())
G = [list(input().rstrip()) for _ in range(n)]
px, py = 0, 0
H = []
for i in range(n):
    for j in range(n):
        if G[i][j] == 'P':
            px, py = i, j
        elif G[i][j] == 'K':
            H.append((i, j))

height = [list(map(int, input().split())) for _ in range(n)]
height_ = sorted({h for row in height for h in row})
m = len(height_)
kCnt = len(H)

while l < m and r < m:
    if calc(height_[l], height_[r]):
        ans = min(ans, height_[r] - height_[l])
        l += 1
    else:
        r += 1
        if r == m:
            break

print(ans)