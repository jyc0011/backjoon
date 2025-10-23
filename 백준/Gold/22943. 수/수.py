import sys
from itertools import permutations

input = sys.stdin.readline

def calc1(n):
    for p1 in range(2, n // 2 + 1):
        p2 = n - p1
        if p1 != p2 and isP[p1] and isP[p2]:
            return True
    return False

def calc2(n):
    remainder = n
    while remainder > 0 and remainder % M == 0:
        remainder //= M
    if remainder <= 1:
        return False
        
    for p1 in range(2, int(remainder**0.5) + 1):
        if remainder % p1 == 0:
            p2 = remainder // p1
            if isP[p1] and isP[p2]:
                return True
    return False

K, M = map(int, input().split())

MAX_NUM = 10**K
isP = [True] * MAX_NUM
isP[0] = isP[1] = False
for i in range(2, int(MAX_NUM**0.5) + 1):
    if isP[i]:
        for j in range(i * i, MAX_NUM, i):
            isP[j] = False

arr = range(10) 
p = permutations(arr, K)
ans = 0
for i in p:
    if i[0] == 0:
        continue
    num = int("".join(map(str, i)))
    if calc1(num) and calc2(num):
        ans += 1
print(ans)