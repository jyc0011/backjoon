import sys
from itertools import permutations

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))
add, sub, mul,div = map(int, sys.stdin.readline().rstrip().split())

op = []

op += ['+'] * add
op += ['-'] * sub
op += ['*'] * mul
op += ['/'] * div

max_val = -float('inf')
min_val = float('inf')

for op_seq in set(permutations(op, n-1)):
    result = a[0]
    for i in range(1, n):
        if op_seq[i-1] == '+':
            result += a[i]
        elif op_seq[i-1] == '-':
            result -= a[i]
        elif op_seq[i-1] == '*':
            result *= a[i]
        elif op_seq[i-1] == '/':
            if result < 0:
                result = -(-result // a[i])
            else:
                result //= a[i]

    if result > max_val:
        max_val = result
    if result < min_val:
        min_val = result

print(max_val)
print(min_val)