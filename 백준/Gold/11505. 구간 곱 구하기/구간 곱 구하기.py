import sys
input = sys.stdin.readline
MOD = 1000000007

def calc(x):
    return pow(x, MOD - 2, MOD)

def update(i, factor):
    while i <= N:
        product_sum[i] = (product_sum[i] * factor) % MOD
        i += i & -i

def product_prefix(i):
    result = 1
    while i > 0:
        result = (result * product_sum[i]) % MOD
        i -= i & -i
    return result

def zero_update(i, delta):
    while i <= N:
        zero[i] += delta
        i += i & -i

def zero_prefix(i):
    res = 0
    while i > 0:
        res += zero[i]
        i -= i & -i
    return res

N, M, K = map(int, input().split())
A = [0] * (N + 1)

for i in range(1, N + 1):
    A[i] = int(input().strip())
    
product_sum = [1] * (N + 1)
zero = [0] * (N + 1)

for i in range(1, N + 1):
    val = A[i] if A[i] != 0 else 1
    j = i
    while j <= N:
        product_sum[j] = (product_sum[j] * val) % MOD
        j += j & -j
    if A[i] == 0:
        j = i
        while j <= N:
            zero[j] += 1
            j += j & -j

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        old = A[b]
        A[b] = c
        old_zero = 1 if old == 0 else 0
        new_zero = 1 if c == 0 else 0
        if new_zero - old_zero != 0:
            j = b
            delta = new_zero - old_zero
            while j <= N:
                zero[j] += delta
                j += j & -j
        if old != 0 and c != 0:
            factor = (c * calc(old)) % MOD
        elif old != 0 and c == 0:
            factor = calc(old) % MOD
        elif old == 0 and c != 0:
            factor = c % MOD
        else:
            factor = 1
        j = b
        while j <= N:
            product_sum[j] = (product_sum[j] * factor) % MOD
            j += j & -j
    else:
        cnt_zero = 0
        j = c
        while j:
            cnt_zero += zero[j]
            j -= j & -j
        j = b - 1
        while j:
            cnt_zero -= zero[j]
            j -= j & -j
        
        if cnt_zero > 0:
            sys.stdout.write("0\n")
        else:
            prod = 1
            j = c
            while j:
                prod = (prod * product_sum[j]) % MOD
                j -= j & -j
            prefix = 1
            j = b - 1
            while j:
                prefix = (prefix * product_sum[j]) % MOD
                j -= j & -j
            sys.stdout.write(str(prod * calc(prefix) % MOD) + "\n")