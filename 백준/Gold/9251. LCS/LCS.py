A=input()
B=input()
dp=[[0]*1001 for _ in range(1001)]

ans=0
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1]==B[j-1]: dp[i][j]=dp[i-1][j-1]+1
        else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        ans=max(ans, dp[i][j])
print(ans)