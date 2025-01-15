import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dist(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
def r(i, j):
    nxt = max(i, j) + 1
    if nxt > w:
        return 0
    if D[i][j] != -1:
        return D[i][j]
    p1 = (1, 1) if i == 0 else E[i]
    p2 = (n, n) if j == 0 else E[j]
    c1 = dist(p1, E[nxt]) + r(nxt, j)
    c2 = dist(p2, E[nxt]) + r(i, nxt)
    if c1 < c2:
        D[i][j] = c1
        C[i][j] = 1
    else:
        D[i][j] = c2
        C[i][j] = 2
    return D[i][j]

n = int(input())
w = int(input())
E = [None]
i, j = 0, 0

for _ in range(w):
    E.append(tuple(map(int, input().split())))
    
D = [[-1]*(w+1) for _ in range(w+1)]
C = [[0]*(w+1) for _ in range(w+1)]

print(r(0, 0))

for _ in range(1, w+1):
    car = C[i][j]
    print(car)
    if car == 1:
        i = max(i, j) + 1
    else:
        j = max(i, j) + 1