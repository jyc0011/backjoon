import sys

input = sys.stdin.readline

def solve():
    n, s, e = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    k = int(input())
    min_ = min(s, e)
    max_ = max(s, e)
    kMin = max_ - min_ + 1
    if k < kMin:
        print(0)
        return
    kMax = 0
    for i in range(min_, max_ + 1):
        kMax += a[i]
    for i in range(min_ - 1, 0, -1):
        if a[i + 1] < 2:
            break
        kMax += a[i]
    for i in range(max_ + 1, n + 1):
        if a[i - 1] < 2:
            break
        kMax += a[i]
    if kMin <= k <= kMax:
        print(1)
    else:
        print(0)

solve()