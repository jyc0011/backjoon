import sys

input = sys.stdin.readline
N, M = map(int, input().split())
meats = []

for _ in range(N):
    a, b = map(int, input().split())
    meats.append((b, a))
meats = sorted(meats, key=lambda x: (x[0], -x[1]))

ans = float('inf')
weight, same = 0, 0
flag = False
for i in range(N):
    weight += meats[i][1]
    if i >= 1 and meats[i][0] == meats[i - 1][0]:
        same += meats[i][0]
    else:
        same = 0
    if weight >= M:
        ans = min(ans, meats[i][0] + same)
        flag = True
print(ans if flag else -1)