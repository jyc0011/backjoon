import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

MAX_SUSHI = 200000
pqs = [[] for _ in range(MAX_SUSHI + 1)]

for i in range(N):
    line = list(map(int, input().split()))
    order_ = line[1:]
    for j in order_:
        heapq.heappush(pqs[j], i)
B = list(map(int, input().split()))
eat = [set() for _ in range(N)]
ans = [0] * N
for i in B:    
    pq = pqs[i]
    while pq:
        idx = pq[0]
        if i in eat[idx]:
            heapq.heappop(pq)
        else:
            ans[idx] += 1
            eat[idx].add(i)
            break

print(*ans)