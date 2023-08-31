import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
garden = [list(map(int, input().split())) for _ in range(n)]

# 비용
def get_cost(y, x):
    cost = garden[y][x] + garden[y-1][x] + garden[y+1][x] + garden[y][x-1] + garden[y][x+1]
    return cost
#중복
def is_overlapping(flowers):
    occupied = set()
    for y, x in flowers:
        if (y, x) in occupied or (y-1, x) in occupied or (y+1, x) in occupied or (y, x-1) in occupied or (y, x+1) in occupied:
            return True
        occupied.update({(y, x), (y-1, x), (y+1, x), (y, x-1), (y, x+1)})
    return False

# DFS
def dfs(x, cnt, flowers, cost_sum):
    global answer
    if cnt == 3:
        if not is_overlapping(flowers):
            answer = min(answer, cost_sum)
        return
    for i in range(x, n-1):
        for j in range(1, n-1):
            flowers.append((i, j))
            cost = get_cost(i, j)
            dfs(i, cnt+1, flowers, cost_sum + cost)
            flowers.pop()

answer = float('inf')
dfs(1, 0, [], 0)
print(answer)