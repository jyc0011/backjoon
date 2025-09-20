import sys
from itertools import permutations

input = sys.stdin.readline

def calc1(min_, b1, b2, b3):
    return max(b1[0] + b2[0], b3[0]) * (max(b1[1], b2[1]) + b3[1])

def calc2(min_,b1,b2,b3):
    return (b1[0] + b2[0] + b3[0]) * max(b1[1], b2[1], b3[1])

def solve():
    box=[tuple(map(int, input().split())) for _ in range(3)]
    min_ = float('inf')
    for p in permutations(box):
        for i in range(8):
            b1 = (p[0][1], p[0][0]) if (i & 1) else p[0]
            b2 = (p[1][1], p[1][0]) if (i & 2) else p[1]
            b3 = (p[2][1], p[2][0]) if (i & 4) else p[2]
            min_ = min(min_,calc1(min_,b1,b2,b3))
            min_ = min(min_,calc2(min_,b1,b2,b3))
    print(min_)

T=int(input())
for _ in range(T):
    solve()