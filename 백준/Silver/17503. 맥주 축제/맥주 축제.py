import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())
beers = [tuple(map(int, input().split())) for _ in range(K)]
beers.sort(key=lambda x: x[1])
result = -1
# Σ 간 레벨별로 먹을 수 있는 술 -> 크면 low랑 mid로, 작으면 mid와 high로 
low, high = 1, 2**31 - 1

while low <= high:
    mid = (low + high) // 2
    total = 0
    min_heap = []
    for v, c in beers:
        if c > mid:
            break
        heapq.heappush(min_heap, v)
        total += v
        if len(min_heap) > N:
            total -= heapq.heappop(min_heap)
    if len(min_heap) == N and total >= M:
        result = mid
        high = mid - 1
    else:
        low = mid + 1
print(result)