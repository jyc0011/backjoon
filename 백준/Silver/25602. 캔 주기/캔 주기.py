import sys

N, K = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
R = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]
M = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]
ans = 0

def dfs(day, total_satisfaction):
    global ans
    if day == K:
        ans = max(ans, total_satisfaction)
        return

    for i in range(N):
        for j in range(N):
            if (i == j and A[i] >= 2) or (i != j and A[i] >= 1 and A[j] >= 1):
                A[i] -= 1; A[j] -= 1
                dfs(day + 1, total_satisfaction + R[day][i] + M[day][j])
                A[i] += 1; A[j] += 1

dfs(0, 0)
print(ans)