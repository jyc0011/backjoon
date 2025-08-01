import sys
input = sys.stdin.readline

MOD = 10**9 + 7
MAX = 10**6 + 1

fac = [1] * MAX
inv = [1] * MAX

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fac[n] * inv[r] % MOD * inv[n-r] % MOD

def power(a, b):
    r = 1
    while b:
        if b % 2:
            r = r * a % MOD
        a = a * a % MOD
        b //= 2
    return r

for i in range(1, MAX):
    fac[i] = fac[i-1] * i % MOD
inv[MAX-1] = power(fac[MAX-1], MOD - 2)
for i in range(MAX-2, -1, -1):
    inv[i] = inv[i+1] * (i+1) % MOD

N = int(input())
ans = 0

for k in range(0, N+1, 2):
    c = comb(N, k)
    p2 = power(2, k)
    p24 = power(24, N - k)
    ans = (ans + c * p2 % MOD * p24 % MOD) % MOD

print(ans)