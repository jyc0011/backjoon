import sys
input = sys.stdin.readline

N, K = map(int, input().split())
prev = [0] * (K + 1)
now = [0] * (K + 1)

for i in range(1, N + 1):
    s = [0] + list(map(int, input().split()))
    if i == 1:
        for j in range(1, K + 1):
            now[j] = s[j]
    else:
        max1 = 0
        max1Idx = -1
        max2 = 0
        for k in range(1, K + 1):
            if prev[k] > max1:
                max2 = max1
                max1 = prev[k]
                max1Idx = k
            elif prev[k] > max2:
                max2 = prev[k]
        for j in range(1, K + 1):
            if j == max1Idx:
                now[j] = s[j] + max2
            else:
                now[j] = s[j] + max1
    prev = now[:]
print(max(prev))