import sys
from collections import Counter

N = int(sys.stdin.readline())
size = sorted(list(map(int, sys.stdin.readline().split())))
ans = 0
check = Counter(size)
for i in check:
    if ans < check[i]:
        ans = check[i]
print(ans)