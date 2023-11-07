import sys
import heapq

def dijkstra(cave, N):
    distance = [[float('inf')] * N for _ in range(N)]
    distance[0][0] = cave[0][0]
    
    q = [(cave[0][0], 0, 0)]  # (cost, x, y)
    
    while q:
        cost, x, y = heapq.heappop(q)
        if distance[x][y] < cost:
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                ncost = cost + cave[nx][ny]
                if ncost < distance[nx][ny]:
                    distance[nx][ny] = ncost
                    heapq.heappush(q, (ncost, nx, ny))
    
    return distance[N-1][N-1]

problem_number = 1
while True:
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    min_loss = dijkstra(cave, N)
    print(f"Problem {problem_number}: {min_loss}")
    problem_number += 1