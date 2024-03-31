import sys

input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int, input().split())))

target_to_0 = float('inf')
result = []

for i in range(n - 2):
    l, r = i + 1, n - 1

    while l < r:
        now = A[i] + A[l] + A[r]
        if abs(now) < abs(target_to_0):
            target_to_0 = now
            result = [A[i], A[l], A[r]]
        if now < 0:
            l += 1
        elif now > 0:
            r -= 1
        else:
            break

print(result[0], result[1], result[2])