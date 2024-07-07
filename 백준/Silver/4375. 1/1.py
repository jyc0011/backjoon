def calc(n):
    num = 1
    l = 1
    while True:
        if num % n == 0:
            return l
        num = num * 10 + 1
        l += 1

while True:
    try:
        n = int(input())
        print(calc(n))
    except EOFError:
        break