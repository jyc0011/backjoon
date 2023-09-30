import sys

input = sys.stdin.readline

N = int(input())
d = [int(input()) for _ in range(N)]

p = [0] * (2 * N + 1)
for i in range(2 * N):
    p[i + 1] = p[i] + d[i % N]

ans, total, r = 0, sum(d), 1

for l in range(2 * N):
    while r < 2 * N + 1 and p[r] - p[l] <= total - (p[r] - p[l]):
        ans = max(ans, p[r] - p[l])
        r += 1

print(ans)