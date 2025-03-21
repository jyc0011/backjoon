import sys
from collections import deque

input = sys.stdin.readline

def calc(N, adj):
    color = [-1] * (N + 1) 
    for start in range(1, N + 1):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            while queue:
                curr = queue.popleft()
                for i in adj[curr]:
                    if color[i] == -1:
                        color[i] = 1 - color[curr]
                        queue.append(i)
                    elif color[i] == color[curr]:
                        return False
    return True

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    if calc(N, adj):
        print("YES")
    else:
        print("NO")