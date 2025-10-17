import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = float('inf')
MAX_=int(1e7+1)

isP=[True]*(MAX_)
isP[0]=isP[1]=False
for i in range(2, int(MAX_**0.5)+1):
    if isP[i]:
        for j in range(i * i, MAX_, i):
            isP[j] = False
        
N,M=map(int,input().split())
eCode=[0]+list(map(int,input().split()))
adj=defaultdict(list)
for _ in range(M):
	u,v,w=map(int,input().split())
	if isP[eCode[u]+eCode[v]]:
			adj[u].append((v,w))
			adj[v].append((u,w))
dist=[INF]*(N+1)
dist[1]=0
pq=[(0,1)]
while pq:
	nowDist,nowNode=heapq.heappop(pq)
	if nowDist>dist[nowNode]:
		continue
	for n,w in adj[nowNode]:
		newDist=nowDist+w
		if newDist<dist[n]:
			dist[n]=newDist
			heapq.heappush(pq,(newDist,n))
if dist[N] == INF:
	print("Now where are you?")
else:
	print(dist[N])