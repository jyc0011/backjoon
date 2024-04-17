import sys

for _ in range(int(input())):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    ans=pow(a, b, 10)
    if ans==0:
        ans=10
    print(ans)