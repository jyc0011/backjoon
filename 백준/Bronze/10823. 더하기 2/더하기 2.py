s = []
while True:
    try:
        s.append(input())
    except EOFError:
        break
s = ''.join(s)
numbers = map(int, s.split(','))
print(sum(numbers))
