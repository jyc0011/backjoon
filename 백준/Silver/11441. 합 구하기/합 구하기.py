import sys
input=sys.stdin.readline

n=int(input())
arr = [*map(int,input().split())]
m=int(input())
psum=[0]*(n+1)
for i in range(1,n+1):
    psum[i]=psum[i-1]+arr[i-1]

for i in range(m):
    l, r=map(int,input().split())
    print(psum[r]-psum[l-1])