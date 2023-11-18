li_a=input()
li_b=input()

dp=[[0]*len(li_b) for _ in range(len(li_a))]
ans=0

for i in range(len(li_a)):
    for j in range(len(li_b)):
        if li_a[i]==li_b[j]:
            if i== 0 or j==0:
                dp[i][j]=1
            else:
                dp[i][j] = dp[i-1][j-1]+1
            ans=max(ans,dp[i][j])
print(ans)