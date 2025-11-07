import sys

input = sys.stdin.readline
sys.setrecursionlimit(200000 * 2) 

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    tree = [0] * (n * 4)
    def build(node, start, end):
        if start == end:
            tree[node] = a[start]
            return
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = max(tree[node * 2], tree[node * 2 + 1])
    def query(node, start, end, left, right):
        if left > end or right < start:
            return -1
        if left <= start and end <= right:
            return tree[node]
        mid = (start + end) // 2
        return max(query(node * 2, start, mid, left, right), 
                   query(node * 2 + 1, mid + 1, end, left, right))
    build(1, 0, n - 1)
    valIndices = {}
    for i in range(n):
        val = a[i]
        if val not in valIndices:
            valIndices[val] = []
        valIndices[val].append(i)
    isStrange = True
    for val, indices in valIndices.items():
        if len(indices) >= 2:
            for k in range(len(indices) - 1):
                i = indices[k]
                j = indices[k+1]
                if i + 1 <= j - 1:
                    rangeMax = query(1, 0, n - 1, i + 1, j - 1)
                    if rangeMax > val:
                        isStrange = False
                        break
        if not isStrange:
            break
    if isStrange:
        print("Yes")
    else:
        print("No")
t = int(input())
for _ in range(t):
    solve()