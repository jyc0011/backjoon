import sys

S,C=map(int,sys.stdin.readline().rstrip().split())
L=[int(sys.stdin.readline().rstrip()) for _ in range(S)]

min_L=1
max_L=max(L)

while min_L<=max_L:
    mid=(min_L+max_L)//2
    Fa=sum(f//mid for f in L)
    if Fa >=C:
        min_L=mid+1
    else:
        max_L=mid-1

ans=sum(L)-(C*max_L)

print(ans)