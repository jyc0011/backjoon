import sys

n,m=map(int,sys.stdin.readline().split())
a=[0]*(n+1)

for i in range(m):
    b,c= map(int,sys.stdin.readline().split())
    a[b]+=1
    a[c]+=1
    
for j in range(1,n+1):
    print(a[j])