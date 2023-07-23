import sys

n,m=map(int,sys.stdin.readline().split())
s=set()
a=0
for i in range(n):
    s.add(sys.stdin.readline().rstrip())
for i in range(m):
    if sys.stdin.readline().rstrip() in s:
        a+=1
print(a)    