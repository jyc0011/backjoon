import sys
from collections import deque

input = sys.stdin.readline

MAX_ = 100001
time = [-1] * MAX_
parent = [0] * MAX_ 

N, K = map(int, input().split())

if K <= N:
    print(N - K)
    print(*range(N, K - 1, -1))
    sys.exit(0)

q = deque([K])
time[K] = 0

while q:
    now = q.popleft()
    if now == N:
        break
    temp = [now + 1, now - 1]
    if now > 0 and now % 2 == 0:
        temp.append(now // 2)
    for nxt in temp:
        if 0 <= nxt < MAX_ and time[nxt] == -1:
            time[nxt] = time[now] + 1
            parent[nxt] = now 
            q.append(nxt)
print(time[N])

path = deque()
curr = N
while curr != K:
    path.append(curr)
    curr = parent[curr]
path.append(K)
print(*path)