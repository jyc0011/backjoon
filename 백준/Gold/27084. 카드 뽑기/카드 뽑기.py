import sys
from collections import Counter
MOD = 10**9 + 7
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
cnt = Counter(A)
sum_ = 1
for c in cnt.values():
    sum_ = (sum_ * (c + 1)) % MOD
ans = (sum_ - 1 + MOD) % MOD
print(ans)