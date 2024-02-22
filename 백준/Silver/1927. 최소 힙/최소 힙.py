import heapq

def min_h(li):
    min_heap = []
    result = []

    for op in li:
        if op == 0:
            if min_heap:
                result.append(heapq.heappop(min_heap))
            else:
                result.append(0)
        else:
            heapq.heappush(min_heap, op)

    return result

n = int(input())
li = [int(input()) for _ in range(n)]

result = min_h(li)
for value in result:
    print(value)