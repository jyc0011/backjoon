import sys

input=sys.stdin.readline

n,k=map(int, input().split())
t=list(map(int, input().split()))
max_ = now = sum(t[:k])
    
for i in range(k, n):
    now += t[i] - t[i-k]
    max_ = max(max_, now)
    
print(max_)