def palindrome(s):
    return s==s[::-1]

r=palindrome(input())

if r==True:
    print("true")
else:
    print("false")