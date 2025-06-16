import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    li = [a**2,b**2,c**2]
    li.sort()
    if li[0]+li[1]==li[2]:
        print("right")
    else:
        print("wrong")