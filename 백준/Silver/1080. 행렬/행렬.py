import sys

def flip(matrix, x, y):
    for i in range(3):
        for j in range(3):
            matrix[x + i][y + j] ^= 1  # XOR

def calc(a, b, n, m):
    if n < 3 or m < 3:
        return -1 if a != b else 0
    cnt = 0
    
    for i in range(n - 2):
        for j in range(m - 2):
            if a[i][j] != b[i][j]:
                flip(a, i, j)
                cnt += 1
                
    if a == b:
        return cnt
    return -1
    
n, m = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
B = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
print(calc(A, B, n, m))