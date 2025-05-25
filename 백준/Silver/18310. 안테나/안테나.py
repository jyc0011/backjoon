import sys
input = sys.stdin.readline

N = int(input())
h = list(map(int, input().split()))
h.sort()
print(h[(N - 1) // 2])