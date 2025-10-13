import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
li = [len(input().rstrip()) for _ in range(n)]
name = [0] * 21 
ans = 0

for i in range(n):
    if i > k:
        name[li[i - k - 1]] -= 1
    nowL = li[i]
    ans += name[nowL]
    name[nowL] += 1
print(ans)