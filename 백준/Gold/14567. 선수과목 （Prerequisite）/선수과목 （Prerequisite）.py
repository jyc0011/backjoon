import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

global ans

def calc(i):
    pre=preq[i]
    if not pre:
        ans[i]=1
    else:
        temp=0
        for node in pre:
            if ans[node] == -1:
                calc(node)
            temp=max(temp,ans[node])
        ans[i]=temp+1

N,M=map(int,input().split())
preq=[[] for _ in range(N+1)]

for _ in range(M):
    A,B=map(int,input().split())
    preq[B].append(A)

ans=[-1]*(N+1)

for i in range(1,N+1):
    calc(i)

print(*ans[1:])