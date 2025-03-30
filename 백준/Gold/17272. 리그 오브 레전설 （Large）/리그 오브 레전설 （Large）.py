import sys
input = sys.stdin.readline
MOD = 10**9 + 7

def mul_(a, b):
    size = len(a)
    res = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
    return res

def pow_(mat, exp):
    size = len(mat)
    res = [[int(i==j) for j in range(size)] for i in range(size)]  # 단위 행렬
    while exp:
        if exp % 2 == 1:
            res = mul_(res, mat)
        mat = mul_(mat, mat)
        exp //= 2
    return res

N, M = map(int,input().split())
if N < M:
    print(1)
    sys.exit()
    
init = [1] * M
T = [[0]*M for _ in range(M)]
T[0][0] = 1 
T[0][M-1] = 1

for i in range(1, M):
    T[i][i-1] = 1
    
T_exp = pow_(T, N - M + 1)
result = 0

for i in range(M):
    result = (result + T_exp[0][i] * init[i]) % MOD
    
print(result)