import sys

input = sys.stdin.readline
NUM = 10**18

Q = int(input())
l, r = -NUM - 1, NUM + 1
p = -1
g = -1

for i in range(1, Q + 1):
    x_str, y = input().split()
    x = int(x_str)
    if y == 'v':
        if r > x:
            r = x
    else:
        if x > l:
            l = x
    if p == -1 and (r - l < 2 or l >= NUM or r <= -NUM):
        p = i
    if g == -1 and l + 2 == r:
        g = i
        
if p != -1:
    print("Paradox!")
    print(p)
elif g != -1:
    print("I got it!")
    print(g)
else:
    print("Hmm...")