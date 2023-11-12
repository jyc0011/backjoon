import sys
import heapq

input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().rstrip())) for _ in range(n)]
costs = [[float('inf')] * n for _ in range(n)]

def find_path():
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = [(0, 0, 0)]
    costs[0][0] = 0

    while queue:
        cost, x, y = heapq.heappop(queue)
        if x == n - 1 and y == n - 1:
            return cost

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and costs[nx][ny] == float('inf'):
                new_cost = cost + (1 if grid[nx][ny] == 0 else 0)
                if new_cost < costs[nx][ny]:
                    costs[nx][ny] = new_cost
                    heapq.heappush(queue, (new_cost, nx, ny))

    return float('inf')

print(find_path())
