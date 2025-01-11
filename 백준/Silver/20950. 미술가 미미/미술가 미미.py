import sys
from itertools import combinations

input = sys.stdin.readline

def calc(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def mix(paints, target):
    cnt = float('inf')
    for r in range(2, 8):
        for combo in combinations(paints, r):
            r_ = sum(color[0] for color in combo) // r
            g_ = sum(color[1] for color in combo) // r
            b_ = sum(color[2] for color in combo) // r
            diff = calc((r_, g_, b_), target)
            cnt = min(cnt, diff)
    return cnt

n = int(input())
paints = [tuple(map(int, input().split())) for _ in range(n)]
target = tuple(map(int, input().split()))
cnt = mix(paints, target)
print(cnt)