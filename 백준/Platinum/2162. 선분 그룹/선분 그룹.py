import sys
from itertools import combinations

input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])

def line_intersection(p1, p2, p3, p4):
    cross1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    cross2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if cross1 == cross2 == 0:
        if (min(p1[0], p2[0]) <= max(p3[0], p4[0])
                and min(p3[0], p4[0]) <= max(p1[0], p2[0])
                and min(p1[1], p2[1]) <= max(p3[1], p4[1])
                and min(p3[1],p4[1]) <= max(p1[1], p2[1])):
            return 1
    elif cross1 <= 0 and cross2 <= 0:
        return 1
    return 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
parent = list(range(n + 1))
lines = [list(map(int, input().split())) for _ in range(n)]

for (i, line1), (j, line2) in combinations(enumerate(lines), 2):
    p1, p2, p3, p4 = line1[:2], line1[2:], line2[:2], line2[2:]
    if line_intersection(p1, p2, p3, p4):
        union(i + 1, j + 1)

groups = [find(i) for i in range(1, n + 1)]
unique_groups = set(groups)
max_group_size = max(groups.count(x) for x in unique_groups)

print(len(unique_groups))
print(max_group_size)