import sys
from collections import deque

def solve():
    k = int(input())
    if k == 1:
        return 0
    queue = deque([(k, 0)])
    visited = {k}
    while queue:
        now, cnt = queue.popleft()
        nextAdd = now + 1
        if nextAdd not in visited:
            visited.add(nextAdd)
            queue.append((nextAdd, cnt + 1))
        if now % 2 == 0:
            nextDiv = now // 2
            if nextDiv == 1:
                return cnt + 1
            if nextDiv > 0 and nextDiv not in visited:
                visited.add(nextDiv)
                queue.append((nextDiv, cnt + 1))
			
T=int(input())
for _ in range(T):
	print(solve())