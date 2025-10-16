import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    adj[i] = temp[:-1]
    degree[i] = len(adj[i])
M = int(input())
believeI = list(map(int, input().split()))
q = deque()
ans = [-1] * (N + 1)
rumor = [0] * (N + 1)
for believer in believeI:
    ans[believer] = 0
    q.append(believer)
while q:
    person = q.popleft()
    now = ans[person]
    for neighbor in adj[person]:
        if ans[neighbor] == -1:
            rumor[neighbor] += 1
            if rumor[neighbor] * 2 >= degree[neighbor]:
                ans[neighbor] = now + 1
                q.append(neighbor)
print(*ans[1:])