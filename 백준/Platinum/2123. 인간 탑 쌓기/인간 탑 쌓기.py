import sys
input = sys.stdin.readline

N = int(input())
a = []
for _ in range(N):
    W, S = map(int, input().split())
    a.append((W, S))
a.sort(key=lambda x: x[0] + x[1])
max_ = -float('inf')
total = 0
for w, s in a:
    now = total - s
    max_ = max(max_, now)
    total += w
print(max_)