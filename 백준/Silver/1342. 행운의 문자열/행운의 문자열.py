import sys
input=sys.stdin.readline

def dfs(N,P):
    global ans
    if N==0:
        ans+=1
        return
    for i in range(26):
        if li[i]>0 and i!=P:
            li[i]-=1
            dfs(N-1,i)
            li[i]+=1

S=list(input().rstrip())
N=len(S)
li=[0]*26
ans=0
for s in S:
    li[ord(s)-ord('a')]+=1
dfs(N,-1)
print(ans)