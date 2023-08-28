import sys

input=sys.stdin.readline
N = int(input())
books = [int(input()) for _ in range(N)]

count = 0
expected = N

for i in range(N-1, -1, -1):
    if books[i] == expected:
        expected -= 1
    else:
        count += 1

print(count)
