import heapq
import sys

n,k=map(int, sys.stdin.readline().rstrip().split())
MAX = 200000
dist = [float('inf')] * (MAX + 1)
pq = []
heapq.heappush(pq, (0, n))
dist[n] = 0

while pq:
    t, x = heapq.heappop(pq)
    if x > 0 and t + 1 < dist[x - 1]:
        dist[x - 1] = t + 1
        heapq.heappush(pq, (t + 1, x - 1))
    if x < MAX and t + 1 < dist[x + 1]:
        dist[x + 1] = t + 1
        heapq.heappush(pq, (t + 1, x + 1))
    if x * 2 <= MAX and t < dist[x * 2]:
        dist[x * 2] = t
        heapq.heappush(pq, (t, x * 2))

print(dist[k])  