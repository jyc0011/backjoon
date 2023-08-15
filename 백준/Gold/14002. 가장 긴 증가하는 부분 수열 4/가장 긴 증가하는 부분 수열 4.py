n=int(input())
A=list(map(int,input().split()))
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if A[i]>A[j]: dp[i]=max(dp[i],dp[j]+1)


ans=[]

std=max(dp) 
print(std)

for i in range(n-1,-1,-1):
        if dp[i]==std:
            ans.append(A[i])
            std-=1

for i in ans[::-1]:
    print(i,end=' ')