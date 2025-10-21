import sys
input = sys.stdin.readline

N = int(input())
MOD = int(1e9+7)

def mat_mul(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def mat_pow(A, n):
    res = [[1, 0], [0, 1]]
    
    while n > 0:
        if n % 2 == 1:
            res = mat_mul(res, A)
        A = mat_mul(A, A)
        n //= 2
    return res

if N == 1:
    print(3)
else:
    T = [[1, 2], [1, 1]]
    v1 = [[1], [1]] 
    M = mat_pow(T, N - 1)
    A_N = (M[0][0] * v1[0][0] + M[0][1] * v1[1][0]) % MOD
    B_N = (M[1][0] * v1[0][0] + M[1][1] * v1[1][0]) % MOD
    answer = (A_N + 2 * B_N) % MOD
    print(answer)