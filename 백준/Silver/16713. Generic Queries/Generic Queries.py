import sys

def xor(a):
    prefix = [0]
    for val in a:
        prefix.append(prefix[-1] ^ val)
    return prefix

input = sys.stdin.readline

n, q = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))
result = 0

prefix = xor(a)

for _ in range(q):
    s, e = map(int, input().rstrip().split())
    result ^= (prefix[e] ^ prefix[s-1])

print(result)