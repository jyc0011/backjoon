import sys, bisect

input = sys.stdin.readline
MAX_ = 61
pow2 = [1 << i for i in range(MAX_ + 1)]
vals, pair = [], {}
for y in range(MAX_ + 1):
    for x in range(y + 1):
        temp = pow2[x] + pow2[y]
        if temp not in pair:
            pair[temp] = (x, y)
            vals.append(temp)
vals.sort()

n = int(input())

for _ in range(n):
    m = int(input())
    idx = bisect.bisect_left(vals, m)
    num = vals[0]
    best_diff = abs(num - m)
    if idx < len(vals):
        diff = abs(vals[idx] - m)
        if diff < best_diff or (diff == best_diff and vals[idx] < num):
            num, best_diff = vals[idx], diff
    if idx:
        left = vals[idx - 1]
        diff = abs(left - m)
        if diff < best_diff or (diff == best_diff and left < num):
            num = left
    x, y = pair[num]
    print(x,y)