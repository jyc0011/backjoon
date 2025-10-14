from collections import defaultdict, deque

def solution(storage, reqs):
    n, m = len(storage), len(storage[0])
    grid = [list(row) for row in storage]
    EMPTY = '0'
    pos = defaultdict(set)
    for r in range(n):
        for c in range(m):
            pos[grid[r][c]].add((r, c))
    answer = n * m
    for r_str in reqs:
        typ = r_str[0]
        if len(r_str) == 2:
            locations = pos[typ].copy()
            if not locations: continue
            
            answer -= len(locations)
            for cr, cc in locations:
                grid[cr][cc] = EMPTY
            pos[typ].clear()
        else:
            outside_cells = set()
            q = deque()
            for r in range(n):
                for c in range(m):
                    if grid[r][c] == EMPTY and (r == 0 or r == n - 1 or c == 0 or c == m - 1):
                        if (r, c) not in outside_cells:
                            q.append((r, c))
                            outside_cells.add((r, c))
            while q:
                cr, cc = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == EMPTY and (nr, nc) not in outside_cells:
                        outside_cells.add((nr, nc))
                        q.append((nr, nc))
            to_remove = []
            locations = pos[typ].copy()
            if not locations: continue
            for cr, cc in locations:
                if cr == 0 or cr == n - 1 or cc == 0 or cc == m - 1:
                    to_remove.append((cr, cc))
                    continue
                is_accessible = False
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (cr + dr, cc + dc) in outside_cells:
                        is_accessible = True
                        break
                if is_accessible:
                    to_remove.append((cr, cc))
            if to_remove:
                answer -= len(to_remove)
                for cr, cc in to_remove:
                    grid[cr][cc] = EMPTY
                    pos[typ].remove((cr, cc))
    return answer