import sys
input = sys.stdin.readline

def sums(photo, R, C):
    sum_arr = [[0] * (C + 1) for _ in range(R + 1)]

    for r in range(1, R + 1):
        for c in range(1, C + 1):
            sum_arr[r][c] = photo[r - 1][c - 1] + sum_arr[r - 1][c] + sum_arr[r][c - 1] - sum_arr[r - 1][c - 1]

    return sum_arr

def avg(sum_arr, r1, c1, r2, c2):
    total = sum_arr[r2][c2] - sum_arr[r1 - 1][c2] - sum_arr[r2][c1 - 1] + sum_arr[r1 - 1][c1 - 1]
    count = (r2 - r1 + 1) * (c2 - c1 + 1)
    return total // count

R, C, Q = map(int, input().rstrip().split())
photo = [list(map(int, input().rstrip().split())) for _ in range(R)]

sum_arr = sums(photo, R, C)

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().strip().split())
    print(avg(sum_arr, r1, c1, r2, c2))