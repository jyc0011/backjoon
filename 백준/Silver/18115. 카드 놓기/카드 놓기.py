from collections import deque

n = int(input())
A = list(map(int, input().split()))
table = deque(range(1, n+1)) 
cards = deque()

for i in range(n):
    top = table.popleft()
    way = A[n-1-i]
    if way == 1:
        cards.appendleft(top)
    elif way == 2:
        first = cards.popleft()
        cards.appendleft(top)
        cards.appendleft(first)
    else:
        cards.append(top)
print(*cards)