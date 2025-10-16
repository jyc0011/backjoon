import sys
input=sys.stdin.readline

n, m = map(int, input().split())
A=list(map(int,input().split()))
prefixSum=[0] * m
prefixSum[0] = A[0]
for i in range(1,m):
    prefixSum[i] = prefixSum[i-1] + A[i]

for _ in range(n):
    want=int(input())
    if want > prefixSum[m-1]:
        print("Go away!")
        continue
    l,r,ans=0,m-1,0
    while l<=r:
        mid=(l+r)//2
        if want<=prefixSum[mid]:
            ans=mid+1
            r=mid-1
        else :
            l=mid+1
    print(ans)