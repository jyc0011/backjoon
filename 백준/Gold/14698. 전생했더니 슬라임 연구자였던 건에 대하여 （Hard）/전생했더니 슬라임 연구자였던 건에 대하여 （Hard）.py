import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    heapq.heapify(s)
    r = 1
    p = 10**9 + 7
    
    while len(s) > 1:
        s1 = heapq.heappop(s)
        s2 = heapq.heappop(s)
        r *= (s1 * s2) % p
        r %= p
        heapq.heappush(s, s1 * s2)

    print(r)