import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def calc(target):
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == target:
            return 1
        elif A[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return 0

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
Q = list(map(int, input().split()))

for question in Q:
    print(calc(question))