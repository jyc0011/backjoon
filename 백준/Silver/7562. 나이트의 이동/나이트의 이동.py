import sys
from collections import deque

input=sys.stdin.readline

d=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

T=int(input())

for _ in range(T):
    l=int(input())
    start=tuple(map(int,input().split()))
    end=tuple(map(int,input().split()))
    
    if start == end:
        print("0")

    visited = [[False] * l for _ in range(l)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, moves = queue.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                if (nx, ny) == end:
                    print(moves + 1)
                
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))