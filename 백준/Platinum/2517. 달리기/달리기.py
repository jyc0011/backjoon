from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
lists = [int(input()) for _ in range(N)]
rank = sorted(lists)
lists = [bisect_left(rank, r)+1 for r in lists]
tree = [0] * (N+1)

def search(idx, length) :
    ans = 0
    while idx :
        ans += tree[idx]
        idx -= idx & -idx
    print(length + 1 - ans)

def update(idx) :
    while idx <= N :
        tree[idx] += 1
        idx += idx & -idx

for i in range(N) :
    search(lists[i], i)
    update(lists[i])