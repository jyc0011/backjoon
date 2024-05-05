import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
p = [tuple(map(int, input().split())) for _ in range(m)]
s = defaultdict(list)
check = [0] * (n + 1)
boss = None

for i in range(n):
    if li[i] == -1:
        boss = i + 1
    else:
        s[li[i]].append(i + 1)

for emp, praise in p:
    check[emp] += praise

queue = deque([boss])
while queue:
    parent = queue.popleft()
    for child in s[parent]:
        check[child] += check[parent]
        queue.append(child)

print(' '.join(map(str, check[1:])))