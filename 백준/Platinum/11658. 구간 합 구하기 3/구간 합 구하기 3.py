import sys

input = sys.stdin.readline

def update(prefix, x, y, diff, n):
    i = x
    while i <= n:
        j = y
        while j <= n:
            prefix[i][j] += diff
            j += (j & -j)
        i += (i & -i)

def query(prefix, x, y):
    s = 0
    i = x
    while i > 0:
        j = y
        while j > 0:
            s += prefix[i][j]
            j -= (j & -j)
        i -= (i & -i)
    return s

def calc(prefix, x1, y1, x2, y2):
    return (query(prefix, x2, y2) - query(prefix, x2, y1 - 1) - query(prefix, x1 - 1, y2) + query(prefix, x1 - 1, y1 - 1) )

n, m = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        update(prefix, i, j, graphs[i-1][j-1], n)
for _ in range(m):
    line = list(map(int, input().split()))
    if line[0] == 0:
        _, x, y, c = line
        old_value = graphs[x-1][y-1]
        diff = c - old_value
        graphs[x-1][y-1] = c
        update(prefix, x, y, diff, n)
    else:
        _, x1, y1, x2, y2 = line
        print(calc(prefix, x1, y1, x2, y2))