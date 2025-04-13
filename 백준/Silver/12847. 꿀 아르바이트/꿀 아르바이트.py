import sys
input = sys.stdin.readline

n, m = map(int, input().split())
T = list(map(int, input().split()))

if m == 0:
    print(0)
    exit()
preffix = sum(T[:m])
max_ = preffix
for i in range(m, n):
    preffix = preffix - T[i - m] + T[i]
    max_ = max(max_, preffix)

print(max_)