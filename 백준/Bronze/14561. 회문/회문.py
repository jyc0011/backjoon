def convert(n, b):
    T = "0123456789ABCDEF"
    q, r = divmod(n, b)
    if q == 0:
        return T[r]
    else:
        return convert(q, b) + T[r]
    
def palindrome(s):
    return s==s[::-1]
    
T=int(input())
for i in range(T):
    N, B = map(int, input().split())
    if palindrome(str(convert(N, B))):
        print("1")
    else:
        print("0")