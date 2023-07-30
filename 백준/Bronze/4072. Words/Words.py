while True:
    s = input()
    if s == '#':
        break
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i][::-1]
    print(' '.join(s))