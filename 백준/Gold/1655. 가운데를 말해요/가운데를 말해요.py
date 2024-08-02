import heapq
import sys

input = sys.stdin.readline

def find_medians(n, numbers):
    max_heap = []
    min_heap = []

    medians = []

    for i in range(n):
        num = numbers[i]

        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if min_heap and -max_heap[0] > min_heap[0]:
            max_val = -heapq.heappop(max_heap)
            min_val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -min_val)
            heapq.heappush(min_heap, max_val)

        medians.append(-max_heap[0])
    
    return medians

n = int(input().strip())
numbers = [int(input().strip()) for _ in range(n)]
medians = find_medians(n, numbers)

for median in medians:
    print(median)