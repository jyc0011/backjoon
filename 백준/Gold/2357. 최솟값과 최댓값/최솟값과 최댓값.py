import sys
input = sys.stdin.readline

MAX = 1000000000

def min_tree(node, start, end):
    if start == end:
        tree_min[node] = arr[start]
    else:
        mid = (start + end) // 2
        min_tree(node*2, start, mid)
        min_tree(node*2+1, mid+1, end)
        tree_min[node] = min(tree_min[node*2], tree_min[node*2+1])

def max_tree(node, start, end):
    if start == end:
        tree_max[node] = arr[start]
    else:
        mid = (start + end) // 2
        max_tree(node*2, start, mid)
        max_tree(node*2+1, mid+1, end)
        tree_max[node] = max(tree_max[node*2], tree_max[node*2+1])

def get_min(node, start, end, left, right):
    if right < start or end < left:
        return MAX
    if left <= start and end <= right:
        return tree_min[node]
    mid = (start + end) // 2
    lmin = get_min(node*2, start, mid, left, right)
    rmin = get_min(node*2+1, mid+1, end, left, right)
    return min(lmin, rmin)

def get_max(node, start, end, left, right):
    if right < start or end < left:
        return -1
    if left <= start and end <= right:
        return tree_max[node]
    mid = (start + end) // 2
    lmax = get_max(node*2, start, mid, left, right)
    rmax = get_max(node*2+1, mid+1, end, left, right)
    return max(lmax, rmax)

N, M = map(int, input().split())
arr = [0]*(N+1)
for i in range(1, N+1):
    arr[i] = int(input())
tree_min = [0]*(4*N)
tree_max = [0]*(4*N)

min_tree(1, 1, N)
max_tree(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    print(get_min(1, 1, N, a, b), get_max(1, 1, N, a, b))