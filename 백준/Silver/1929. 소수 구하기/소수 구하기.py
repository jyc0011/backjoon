m, n = map(int, input().split())

if m < 2:
    m = 2

a = [True] * (n + 1)
a[0], a[1] = False, False

for i in range(2, int(n**0.5) + 1):
    if a[i]:
        for j in range(i * i, n + 1, i):
            a[j] = False

for i in range(m, n + 1):
    if a[i]:
        print(i)