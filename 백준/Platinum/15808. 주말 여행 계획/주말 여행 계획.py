import heapq
import sys

input = sys.stdin.readline
MAX = 1000000000
ans = MAX
n = int(input())
adj = [list(map(int, input().strip().split())) for _ in range(n)]
p, q = map(int, input().strip().split())
tour = [tuple(map(int, input().strip().split())) for _ in range(p)]
hotel = [tuple(map(int, input().strip().split())) for _ in range(q)]
dist = [MAX] * n
pq = []

for x, y in tour:
    x -= 1
    dist[x] = -y
    heapq.heappush(pq, (dist[x], x))
    
cnt = [0] * n
for x, y in hotel:
    x -= 1
    cnt[x] = y

while pq:
    w, v = heapq.heappop(pq)
    if dist[v] < w:
        continue
    for i in range(n):
        if adj[v][i] == 0:
            continue
        if dist[i] > adj[v][i] + w:
            dist[i] = adj[v][i] + w
            heapq.heappush(pq, (dist[i], i))

for i in range(n):
    if cnt[i]:
        ans = min(ans, dist[i] - cnt[i])
    
print(-ans)