import sys

p = {2, 3, 5, 7, 11, 13, 17}
ans = 0
max_ = 100000
cnt = [0] * (max_ + 1)

for i in range(2, max_ + 1):
    if cnt[i] == 0:
        for j in range(i, max_ + 1, i):
            temp = j
            while temp % i == 0:
                cnt[j] += 1
                temp //= i
                
A, B = map(int, sys.stdin.readline().split())
for i in range(A, B + 1):
    if cnt[i] in p:
        ans += 1

print(ans)