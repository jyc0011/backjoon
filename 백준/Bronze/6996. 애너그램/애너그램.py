import sys

n=int(sys.stdin.readline())

for i in range(n):
    a,b=sys.stdin.readline().split()
    if sorted(a)==sorted(b):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")