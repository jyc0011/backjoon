import sys
input = sys.stdin.readline

def update(bit, i, diff):
    while i <= N:
        bit[i] += diff
        i += (i & -i)

def query(bit, i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= (i & -i)
    return res

def find_k(bit, k):
    l, r = 1, N
    while l < r:
        mid = (l + r) // 2
        if query(bit, mid) >= k:
            r = mid
        else:
            l = mid + 1
    return l

N = int(input())
W = list(map(int, input().split()))
P = list(map(int, input().split()))

bit = [0] * (N + 2)

for i in range(N):
    update(bit, i + 1, W[i])

result = []
for pi in P:
    idx = find_k(bit, pi)
    result.append(idx)
    update(bit, idx, -W[idx - 1])

print(*result)