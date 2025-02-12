from collections import deque

def bfs(board, val, N):
    seen = [[False] * N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == val and not seen[i][j]:
                q = deque([(i, j)])
                seen[i][j] = True
                grp = []
                while q:
                    x, y = q.popleft()
                    grp.append((x, y))
                    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if not seen[nx][ny] and board[nx][ny] == val:
                                seen[nx][ny] = True
                                q.append((nx, ny))
                groups.append(grp)
    return groups

def norm(grp):
    grp.sort()
    mi, mj = grp[0]
    norm_grp = [(x - mi, y - mj) for x, y in grp]
    norm_grp.sort()
    return norm_grp

def rot(grp):
    new_grp = [(y, -x) for x, y in grp]
    return norm(new_grp)

def all_rots(grp):
    rots = []
    cur = grp
    for _ in range(4):
        cur = norm(cur)
        rots.append(cur)
        cur = rot(cur)
    return rots
    
def solution(game, table):
    N = len(game)
    holes_raw = bfs(game, 0, N)
    pieces_raw = bfs(table, 1, N)
    holes = [norm(grp) for grp in holes_raw]
    pieces = [norm(grp) for grp in pieces_raw]
    res = 0
    used = [False] * len(pieces)
    for hole in holes:
        for i, piece in enumerate(pieces):
            if used[i] or len(piece) != len(hole):
                continue
            for cand in all_rots(piece):
                if cand == hole:
                    used[i] = True
                    res += len(hole)
                    break
            else:
                continue
            break
    return res