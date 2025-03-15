import sys
import bisect
import math
input = sys.stdin.readline

N,M=map(int,input().split())
A=sorted(list(map(int,input().split())))
B=list(map(int,input().split()))
ans = []

for b in B:
    count = bisect.bisect_right(A, b)
    k = math.floor(math.sqrt(count / 3) + 0.5)
    ans.append(k)
    
print(*ans)