import sys

n,m = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

size = min(n, m)
while size > 0:
    for i in range(n - size + 1):
        for j in range(m - size + 1):
            if matrix[i][j] == matrix[i + size - 1][j] == matrix[i][j + size - 1] == matrix[i + size - 1][j + size - 1]:
                print(size * size)
                sys.exit(0)
    size -= 1
print(1)