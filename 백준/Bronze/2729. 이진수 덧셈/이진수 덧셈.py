import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(lambda x: int(x, 2), sys.stdin.readline().split())
    print(bin(a + b)[2:])