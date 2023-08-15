import sys

M, N = map(int, sys.stdin.readline().split())
arr = []

for _ in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    arr.append(data)

s_arr = sorted(arr, key=lambda x: (-x[1], -x[2], -x[3]))

for c in arr:
    if c[0] == N:
        target = c
        break

rank = s_arr.index(target) + 1
print(rank)