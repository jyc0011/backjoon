import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
towers = deque(map(int, input().split()))
li = deque()
ans = [0] * N

for i in range(N):
    temp = towers[i]
    while li and li[-1][0] < temp:
        li.pop()
    if li:
        ans[i] = li[-1][1] + 1
    li.append((temp, i))
print(" ".join(map(str, ans)))