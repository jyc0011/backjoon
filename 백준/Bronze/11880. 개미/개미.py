import sys

T = int(sys.stdin.readline())
for _ in range(T):
    a, b, c = map(int, sys.stdin.readline().split())
    baseA = (a ** 2) + ((b + c) ** 2)
    baseB = (b ** 2) + ((a + c) ** 2)
    baseC = (c ** 2) + ((a + b) ** 2)
    answer = min(baseA, baseB, baseC)
    print(answer)