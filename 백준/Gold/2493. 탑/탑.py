import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
li = []
ans = [0] * N

for i in range(N):
    height = towers[i]
    while li and li[-1][0] < height:
        li.pop()
    if li:
        ans[i] = li[-1][1] + 1
    li.append((height, i))
print(" ".join(map(str, ans)))