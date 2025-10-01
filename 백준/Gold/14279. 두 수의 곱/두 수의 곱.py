import sys

a, b, c = map(int, sys.stdin.readline().split())
ans = float('inf')

for A in range(1, 35000):
    for C in range(A, 2000001, A):
        B = C // A
        cost = abs(A - a) + abs(B - b) + abs(C - c)
        if cost < ans:
            ans = cost
for B in range(1, 35000):
    for C in range(B, 2000001, B):
        A = C // B
        cost = abs(A - a) + abs(B - b) + abs(C - c)
        if cost < ans:
            ans = cost

print(ans)