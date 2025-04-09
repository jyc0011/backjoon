import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

max_prefix = [0] * N
min_prefix = [0] * N
now_max = now_min = P[0]
max_prefix[0] = min_prefix[0] = P[0]

for i in range(1, N):
    now_max = max(P[i], now_max + P[i])
    now_min = min(P[i], now_min + P[i])
    max_prefix[i] = max(max_prefix[i-1], now_max)
    min_prefix[i] = min(min_prefix[i-1], now_min)

max_right = [0] * N
min_right = [0] * N
now_max = now_min = P[-1]
max_right[-1] = min_right[-1] = P[-1]

for i in range(N-2, -1, -1):
    now_max = max(P[i], now_max + P[i])
    now_min = min(P[i], now_min + P[i])
    max_right[i] = max(max_right[i+1], now_max)
    min_right[i] = min(min_right[i+1], now_min)
    
ans = float('-inf')
for i in range(N-1):
    ans = max(ans,
              max_prefix[i] * max_right[i+1],
              min_prefix[i] * min_right[i+1])

print(ans)

# Kadane’s Algorithm