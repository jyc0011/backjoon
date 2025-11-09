from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc, n, m, land, visited):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    size = 0
    cols = set()
    while q:
        r, c = q.popleft()
        size += 1
        cols.add(c)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m:
                if land[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return size, cols

def solution(land):
    n = len(land)
    m = len(land[0])
    col_oil = [0] * m
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size, cols = bfs(i, j, n, m, land, visited)
                for c in cols:
                    col_oil[c] += size
    return max(col_oil)