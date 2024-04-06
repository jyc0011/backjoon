import sys

input=sys.stdin.readline

N, M = map(int, input().split())
ans = 0
prefix_sum = [0]*(N+1)

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + int(input())
    
min_ = 0

for i in range(M, N+1):
    min_ = min(min_, prefix_sum[i-M])
    ans = max(ans, prefix_sum[i]-min_)

print(ans)