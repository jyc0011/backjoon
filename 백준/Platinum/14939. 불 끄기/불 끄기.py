import sys

input=sys.stdin.readline

def flip(grid, r, c):
    for dr, dc in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 10 and 0 <= nc < 10:
            grid[nr][nc] = '#' if grid[nr][nc] == 'O' else 'O'

grid = list(input().rstrip() for _ in range(10))
answer = float('inf')
for first_row in range(1 << 10):
    press_cnt = 0
    temp_grid = [list(row) for row in grid]
    for i in range(10):
        if first_row & (1 << i):
            flip(temp_grid, 0, i)
            press_cnt += 1

    for r in range(1, 10):
        for c in range(10):
            if temp_grid[r - 1][c] == 'O':
                flip(temp_grid, r, c)
                press_cnt += 1

    if all(temp_grid[9][c] == '#' for c in range(10)):
        answer = min(answer, press_cnt)

if answer == float('inf'):
    print(-1)
else :
    print(answer)