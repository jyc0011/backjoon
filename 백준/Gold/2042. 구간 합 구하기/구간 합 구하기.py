import sys

input=sys.stdin.readline

def seg(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        tree[node] = seg(node * 2, start, mid) + seg(node * 2 + 1, mid + 1, end)
    return tree[node]

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)

def sum(n, s, e, l, r):
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return tree[n]
    m = (s + e) // 2
    return sum(n * 2, s, m, l, r) + sum(n * 2 + 1, m + 1, e, l, r)

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * 4 * N

seg(1, 0, N - 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - arr[b]
        arr[b] = c
        update(1, 0, N-1, b, diff)
    else:
        print(sum(1, 0, N-1, b-1, c-1))