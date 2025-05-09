import sys
from collections import deque

input = sys.stdin.readline

LIMIT = 500000
N, K = map(int, input().split())

if N == K:
    print(0)
    sys.exit(0)

visited = [[False]*(LIMIT+1) for _ in range(2)]
visited[0][N] = True
q = deque([N])
time = 0

while True:
    bro = K + time*(time+1)//2
    if bro > LIMIT:
        print(-1)
        break
    if visited[time & 1][bro]:
        print(time)
        break
    time += 1
    for _ in range(len(q)):
        cur = q.popleft()
        for nxt in (cur-1, cur+1, cur*2):
            if 0 <= nxt <= LIMIT and not visited[time & 1][nxt]:
                visited[time & 1][nxt] = True
                q.append(nxt)