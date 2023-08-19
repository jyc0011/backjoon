l = [0, 3, 1, 4, 2]
n = int(input())

i = l[n % 5]
j = (n - 2 * i) // 5 

if j >= 0:
    t = i + j
else:
    t = -1

print(t)