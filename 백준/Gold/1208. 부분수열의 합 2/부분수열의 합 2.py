import sys
from itertools import combinations
from collections import Counter

input = sys.stdin.readline

def calc(li):
    s = Counter()
    s[0] = 1
    for i in range(1, len(li) + 1):
        for comb in combinations(li, i):
            s[sum(comb)] += 1
    return s

N, S = map(int,input().rstrip().split())
num = list(map(int,input().rstrip().split()))

l, r = num[:N//2], num[N//2:]
sum_l = calc(l)
sum_r = calc(r)

ans = 0
for L in sum_l:
    target = S - L
    ans += sum_l[L] * sum_r[target]

print(ans - (1 if S == 0 else 0))