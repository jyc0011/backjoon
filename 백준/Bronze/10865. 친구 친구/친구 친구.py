import sys

n,m=map(int,sys.stdin.readline().split())
li=[0]*n
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    li[a-1]+=1
    li[b-1]+=1
for i in range(n):
    print(li[i])