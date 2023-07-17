import sys

N = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)
for number in numbers:
    print(number)
