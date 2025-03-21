import sys
import heapq

input = sys.stdin.readline

N,M=map(int,input().split())
X=list(map(int, input().split()))
prioty=[]
cnt=0
anger=0

for i in X:
    anger+=i
    heapq.heappush(prioty, -i)
    while anger>=M:
        if not prioty:
            break
        p=heapq.heappop(prioty)
        anger+=p*2
        cnt+=1

print(cnt)