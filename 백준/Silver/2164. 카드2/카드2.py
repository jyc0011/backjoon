from collections import deque

n=int(input())

# 버리고 아래로 -> queue

queue=deque([i for i in range(1,n+1)])

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])