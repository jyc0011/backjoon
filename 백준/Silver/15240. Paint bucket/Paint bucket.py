from collections import deque

def bfs(matrix, y, x, target_color, new_color):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque([(y, x)])
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < rows and 0 <= nx < cols and not visited[ny][nx] and matrix[ny][nx] == target_color:
                visited[ny][nx] = True
                queue.append((ny, nx))
        matrix[cy][cx] = new_color

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
Y, X, K = map(int, input().split())
target_color = matrix[Y][X]
bfs(matrix, Y, X, target_color, str(K))

for row in matrix:
    print("".join(row))