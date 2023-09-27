import sys

def xor(a):
    n = len(a)
    prefix = [0] * n
    prefix[0] = a[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] ^ a[i]
    return prefix

input = sys.stdin.readline

n, q = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))
result = 0

prefix =xor(a)

for _ in range(q):
    s, e = map(int, input().rstrip().split())
    s -= 1
    e -= 1
    if s == 0:
        result ^= prefix[e]
    else:
        result ^= (prefix[e] ^ prefix[s-1])

print(result)
