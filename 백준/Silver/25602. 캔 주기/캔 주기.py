import sys

N, K = map(int, sys.stdin.readline().strip().split())
A = [0] + list(map(int, sys.stdin.readline().strip().split()))
R = [[0] + list(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]
M = [[0] + list(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]
ans = 0

def dfs(d, r, m):
    global ans
    if d > K:
        ans = max(ans, r + m)
        return

    for i in range(1, N + 1):
        nr = r
        nm = m
        if A[i] > 0:
            A[i] -= 1
            nr += R[d-1][i]
            for j in range(1, N + 1):
                if A[j] > 0:
                    A[j] -= 1
                    nm += M[d-1][j]
                    dfs(d + 1, nr, nm)
                    nm -= M[d-1][j]
                    A[j] += 1
            nr -= R[d-1][i]
            A[i] += 1

dfs(1, 0, 0)
print(ans)