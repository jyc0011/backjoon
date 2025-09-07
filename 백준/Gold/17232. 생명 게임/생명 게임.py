import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
K, a, b = map(int, input().split())
ans = [input().rstrip() for _ in range(N)]

for _ in range(T):
    now = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if ans[r][c] == '*':
                now[r][c] = 1
    pref = [[0] * (M + 1) for _ in range(N + 1)]
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            pref[r][c] = now[r-1][c-1] + pref[r-1][c] + pref[r][c-1] - pref[r-1][c-1]
    next = [[''] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            r1, c1 = max(0, r - K), max(0, c - K)
            r2, c2 = min(N - 1, r + K), min(M - 1, c + K)
            total = pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]
            temp = total - now[r][c]
            if now[r][c] == 1: 
                if a <= temp <= b:
                    next[r][c] = '*'
                else:
                    next[r][c] = '.'
            else:
                if a < temp <= b:
                    next[r][c] = '*'
                else:
                    next[r][c] = '.'
    ans = ["".join(row) for row in next]

for row in ans:
    print(row)