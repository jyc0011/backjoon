import sys

input = sys.stdin.readline


def build(node, start, end):
    if start == end:
        seg_tree[node] = start
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        left_idx = seg_tree[node * 2]
        right_idx = seg_tree[node * 2 + 1]
        if A[left_idx] <= A[right_idx]:
            seg_tree[node] = left_idx
        else:
            seg_tree[node] = right_idx

def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return
    if start == end:
        A[idx] = val
        seg_tree[node] = idx
        return
    mid = (start + end) // 2
    if idx <= mid:
        update(node * 2, start, mid, idx, val)
    else:
        update(node * 2 + 1, mid + 1, end, idx, val)
    left_idx = seg_tree[node * 2]
    right_idx = seg_tree[node * 2 + 1]
    if A[left_idx] <= A[right_idx]:
        seg_tree[node] = left_idx
    else:
        seg_tree[node] = right_idx

def min_idx(node, start, end, l, r):
    if r < start or end < l:
        return -1
    if l <= start and end <= r:
        return seg_tree[node]
    mid = (start + end) // 2
    left = min_idx(node * 2, start, mid, l, r)
    right = min_idx(node * 2 + 1, mid + 1, end, l, r)
    if left == -1:
        return right
    if right == -1:
        return left
    if A[left] <= A[right]:
        return left
    else:
        return right

N=int(input())
A=list(map(int, input().split()))
seg_tree=[0]*(4*N)
build(1, 0, N - 1)
M=int(input())

for _ in range(M):
    num, i, k = map(int, input().split())
    if num==1:
        update(1, 0, N - 1, i - 1, k)
    else:
        ans=min_idx(1, 0, N - 1, i - 1,k-1)
        print(ans + 1)