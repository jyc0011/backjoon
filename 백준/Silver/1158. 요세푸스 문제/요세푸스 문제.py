from collections import deque

N, K = map(int, input().split())

queue = deque([i for i in range(1, N + 1)])

print('<', end='')

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
        
print('>')