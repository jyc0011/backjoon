import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque(range(1, N + 1))
discard = []

while len(q) > 1:
    discard.append(q.popleft())
    q.append(q.popleft())

print(*discard, q[0])