empty = 0

def convert(n, b):
    T = "0123456789"
    result = ""
    while n > 0:
        q, r = divmod(n, b)
        result = T[r] + result
        n = q
    return result

def palindrome(s):
    return s == s[::-1]

N = int(input())

for i in range(2, 11):
    cv = convert(N, i)
    if palindrome(cv):
        print(i, cv)
        empty += 1

if empty == 0:
    print("NIE")
