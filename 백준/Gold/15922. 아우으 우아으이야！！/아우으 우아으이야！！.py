import sys
input = sys.stdin.readline

N = int(input())
l_, r_ = map(int, input().split())
ans = 0

for _ in range(N - 1):
    l, r = map(int, input().split())
    if l <= r_:
        if r > r_:
            r_ = r
    else:
        ans += r_ - l_
        l_, r_ = l, r

ans += r_ - l_
print(ans)