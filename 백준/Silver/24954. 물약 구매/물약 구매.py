import sys
from collections import defaultdict

input=sys.stdin.readline

N=int(input())
C=[0]+list(map(int,input().split()))
sales=[[0]*(N+1) for i in range(N+1)]
for i in range(1,N+1):
    p=int(input())
    if p!=0:
        for _ in range(p):
            a,d=map(int,input().split())
            sales[i][a]=d
dp=[-1]*(1<<N)

def solve(mask):
    if mask == (1<<N)-1:
        return 0
    if dp[mask] != -1:
        return dp[mask]
    min_=float('inf')
    for i in range(N):
        if not (mask & (1 <<i)):
            now=C[i+1]
            for j in range(N):
                if mask& (1 <<j):
                    now-=sales[j+1][i+1]
            now=max(1,now)
            ifBuy=now+solve(mask|(1<<i))
            min_=min(min_, ifBuy)
    dp[mask]=min_
    return min_

print(solve(0))