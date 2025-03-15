import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    d = [-1] * (N + 1)
    d[start] = 0

    while queue:
        node = queue.popleft()
        for n in li[node]:
            if d[n] == -1:
                d[n] = d[node] + 1
                queue.append(n)

    return d

N, M = map(int, input().split())
li = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    li[A].append(B)
    li[B].append(A)

d = bfs(1)

max_ = max(d[1:])
num = d.index(max_)
cnt = d.count(max_)

print(num, max_, cnt)