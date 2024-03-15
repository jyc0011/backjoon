import sys
input = sys.stdin.readline

def check(r, c):
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = r, c
        while 0 <= x < n and 0 <= y < n:
            if g[x][y] == 'O': break
            if g[x][y] == 'S': return True
            x += dr
            y += dc
    return False

def dfs(cnt):
    if cnt == 3:
        return all(not check(t[0], t[1]) for t in ts)
    for i in range(n**2):
        x, y = divmod(i, n)
        if g[x][y] == 'X':
            g[x][y] = 'O'
            if dfs(cnt + 1):
                return True
            g[x][y] = 'X'
    return False

n = int(input())
g = [input().split() for _ in range(n)]
ts = [(i, j) for i in range(n) for j in range(n) if g[i][j] == 'T']

print('YES' if dfs(0) else 'NO')