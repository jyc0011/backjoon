import sys

def calc(Li, mid):
    cnt=0
    left=0
    for i in Li:
        if left<i:
            cnt+=1
            left=mid
        left-=i
    return cnt

N,M=map(int,sys.stdin.readline().rstrip().split())
Li=[int(sys.stdin.readline().rstrip()) for _ in range(N)]

min_L=max(Li)
max_L=sum(Li)

while min_L<=max_L:
    mid=(min_L+max_L)//2
    temp=calc(Li,mid)

    if temp >M:
        min_L=mid+1
    else:
        max_L=mid-1

print(min_L)