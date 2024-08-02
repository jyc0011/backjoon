import heapq

def calc(n, m, cards):
    heapq.heapify(cards)
    
    for _ in range(m):
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        val = first + second
        heapq.heappush(cards, val)
        heapq.heappush(cards, val)
    return sum(cards)

n, m = map(int, input().strip().split())
cards = list(map(int, input().strip().split()))

print(calc(n, m, cards))