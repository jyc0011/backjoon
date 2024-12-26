import sys

def sol(n):
    if n == 1:
        return 0
    res = n

    i = 2
    while i * i <= n:
        if n % i == 0:
            res //= i
            res *= (i - 1)
        while n % i == 0:
            n //= i
        i += 1
    if n != 1:
        res //= n
        res *= (n - 1)

    return res

input = sys.stdin.read
data = input().split()
for n_str in data:
    n = int(n_str)
    if n == 0:
        break
    print(sol(n))