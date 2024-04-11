import sys

input=sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def calc(p, N):
    edges = []
    parent = [i for i in range(N)]
    for d in range(3):
        p.sort(key=lambda x: x[d])
        for i in range(N - 1):
            cost = abs(p[i][d] - p[i + 1][d])
            edges.append((cost, p[i][3], p[i + 1][3]))
    edges.sort()
    min_cost = 0
    for cost, p1, p2 in edges:
        if find(parent, p1) != find(parent, p2):
            union(parent, p1, p2)
            min_cost += cost

    return min_cost

N = int(input())
P = [list(map(int, input().split())) + [i] for i in range(N)]

min_cost = calc(P, N)
print(min_cost)
