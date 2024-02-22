import heapq

def max_h(li):
    max_heap = []
    result = []

    for op in li:
        if op == 0:
            if max_heap:
                result.append(-heapq.heappop(max_heap))
            else:
                result.append(0)
        else:
            heapq.heappush(max_heap, -op)

    return result

n = int(input())
li = [int(input()) for _ in range(n)]

result = max_h(li)
for value in result:
    print(value)