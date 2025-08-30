import sys
from collections import deque

input = sys.stdin.readline

MAX_=100001
time=[-1]*MAX_
cnt=[0]*MAX_

N,K=map(int,input().split())

if K <= N :
    print(N-K)
    print(1)
    sys.exit(0)

q=deque([N])
time[N]=0
cnt[N]=1

while q:
    now=q.popleft()
    for nxt in [now-1, now+1, now*2]:
        if 0<=nxt<MAX_:
            if time[nxt]==-1:
                time[nxt]=time[now]+1
                cnt[nxt]=cnt[now]
                q.append(nxt)
            elif time[nxt]==time[now]+1:
                cnt[nxt]+=cnt[now]
                
print(time[K])
print(cnt[K])