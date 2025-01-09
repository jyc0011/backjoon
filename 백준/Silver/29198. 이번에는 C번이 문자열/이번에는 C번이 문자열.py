import sys

input = sys.stdin.readline

def calc(e):
    f, _ = e
    return tuple(-x for x in f)

N, M, K = map(int, input().split())
S = [input().strip() for _ in range(N)]
arr = []
sum_ = [0]*26
ans = []

for s in S:
    temp = [0]*26
    for ch in s:
        temp[ord(ch) - ord('A')] += 1
    arr.append(temp)

idx = [(arr[i], i) for i in range(N)]
idx.sort(key=calc)
chosen = [idx for (_, idx) in idx[:K]]

for i in chosen:
    for j in range(26):
        sum_[j] += arr[i][j]

for j in range(26):
    if sum_[j] > 0:
        ans.append(chr(ord('A') + j) * sum_[j])

print("".join(ans))