import sys
input = sys.stdin.readline

N = int(input())
diff = [0]* (361)

for _ in range(N):
    a, b = map(int, input().split())
    alpha = (a + 180) % 360
    l = (alpha - b) % 360
    r = (alpha + b) % 360

    if l <= r:
        diff[l] += 1
        diff[r + 1] -= 1
    else:
        diff[0] += 1
        diff[r + 1] -= 1
        diff[l] += 1
        diff[360] -= 1
cnt = 0
now = 0
for ang in range(360):
    now += diff[ang]
    if now > 0:
        cnt += 1

print(cnt)