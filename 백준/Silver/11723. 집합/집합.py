import sys

input = sys.stdin.readline
m = int(input())
s = 0

for _ in range(m):
    ops = input().split()
    cmd = ops[0]
    if len(ops) == 2:
        x = int(ops[1]) - 1
    if cmd == 'add':
        s |= 1 << x
    elif cmd == 'remove':
        s &= ~(1 << x)
    elif cmd == 'check':
        print(1 if s & 1 << x else 0)
    elif cmd == 'toggle':
        s ^= 1 << x
    elif cmd == 'all':
        s = (1 << 20) - 1
    elif cmd == 'empty':
        s = 0