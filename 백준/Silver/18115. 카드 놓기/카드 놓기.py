from collections import deque

n = int(input())
A = list(map(int, input().split()))
cards = deque()

for i in range(n):
    way = A[n-1-i]
    if way == 1:
        cards.appendleft(i+1)
    elif way == 2:
        first = cards.popleft()
        cards.appendleft(i+1)
        cards.appendleft(first)
    else:
        cards.append(i+1)
print(*cards)