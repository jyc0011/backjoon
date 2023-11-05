A = int(input())
B = int(input())
C = int(input())

product = A * B * C

count = [str(product).count(str(i)) for i in range(10)]

for c in count:
    print(c)