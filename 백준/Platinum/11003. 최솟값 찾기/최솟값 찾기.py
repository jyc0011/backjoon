import heapq

N, L = map(int, input().split())
A = list(map(int, input().split()))
heap = []

for i in range(L - 1):
    heapq.heappush(heap, (float('inf'), i - (L - 1)))

for i in range(N):
    heapq.heappush(heap, (A[i], i))
    while heap[0][1] < i - L + 1:
        heapq.heappop(heap)
    print(heap[0][0], end=' ')