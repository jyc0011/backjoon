for i in range(int(input())):
    a=int(input())
    b=int(str(a)[::-1])+a
    if b==int(str(b)[::-1]):
        print("YES")
    else:
        print("NO")