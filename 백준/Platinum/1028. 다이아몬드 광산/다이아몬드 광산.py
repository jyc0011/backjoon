import sys

input = sys.stdin.readline

R, C = map(int, input().split(' '))
mine = []
result = 0
for r in range(R):
    mine.append(list(map(int, list(input().rstrip()))))

dp_dr = [[0 for _ in range(C)] for _ in range(R)]
dp_dl = [[0 for _ in range(C)] for _ in range(R)]
dp_ur = [[0 for _ in range(C)] for _ in range(R)]
dp_ul = [[0 for _ in range(C)] for _ in range(R)]

for r in range(R - 1, -1, -1):
    for c in range(C):
        if mine[r][c] == 1:
            if r == R - 1:
                dp_dr[r][c] = 1
                dp_dl[r][c] = 1
            else:
                dp_dr[r][c] = dp_dr[r + 1][c + 1] + 1 if c + 1 <= C - 1 else 1
                dp_dl[r][c] = dp_dl[r + 1][c - 1] + 1 if c - 1 >= 0 else 1

for r in range(R):
    for c in range(C):
        temp = min(dp_dr[r][c], dp_dl[r][c])
        for size in range(temp, 0, -1):
            if size <= result:
                break
            max_p = r + size - 1
            if max_p >= R:
                continue
            min_c, max_c = c - size + 1, c + size - 1
            if min_c < 0 or max_c >= C:
                continue
            if dp_dr[max_p][min_c] >= size and dp_dl[max_p][max_c] >= size:
                result = size

print(result)