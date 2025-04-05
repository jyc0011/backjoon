import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

left = 0
right = 0
ans = float('inf')

while left < N and right < N:
    diff = arr[right] - arr[left]
    if diff < M:
        right += 1
    else:
        ans = min(ans, diff)
        left += 1
    if right < left:
        right = left

print(ans)