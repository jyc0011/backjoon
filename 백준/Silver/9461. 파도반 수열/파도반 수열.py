t = int(input())
li = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11,101):
    li.append(li[i - 2] + li[i - 3])

for _ in range(t):
    n = int(input())
    print(li[n]) 