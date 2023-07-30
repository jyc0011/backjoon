import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    s = input()
    res = ''.join([chr(ord('A') + ((ord(c)-ord('A'))*a + b)%26) for c in s])
    print(res)