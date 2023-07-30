n = int(input())
for _ in range(n):
    name = input()
    g_count = name.lower().count('g')
    b_count = name.lower().count('b')

    if g_count > b_count:
        print(name, 'is GOOD')
    elif b_count > g_count:
        print(name, 'is A BADDY')
    else:
        print(name, 'is NEUTRAL')