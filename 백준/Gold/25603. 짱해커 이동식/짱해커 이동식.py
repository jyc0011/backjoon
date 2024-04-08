import sys
import heapq

input=sys.stdin.readline

n,k=map(int, input().rstrip().split())
cost=list(map(int, input().rstrip().split()))
heap=[]

for i in range(n-k+1):
    li=cost[i:i+k:1]
    heapq.heappush(heap,-min(li))
print(-heapq.heappop(heap))