def convert(n, b):
    T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$"
    q, r = divmod(n, b)
    if q == 0:
        return T[r]
    else:
        return convert(q, b) + T[r]

def palindrome(s):
    return s==s[::-1]

T = int(input())
for _ in range(T):
    N = int(input())
    flag = 0
    for B in range(2, 65):
        if palindrome(convert(N, B)):
            flag = 1
            break
    print(flag)
