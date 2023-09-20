import sys

n, b, w = map(int, sys.stdin.readline().rstrip().split())
stone = sys.stdin.readline().rstrip()

l, r = 0, 0
wn, bn = 0, 0
ml = 0

while r < n:
    if stone[r] == 'W':
        wn += 1
    else:
        bn += 1
    while bn > b:
        if stone[l] == 'W':
            wn -= 1
        else:
            bn -= 1
        l += 1
    if wn >= w:
        ml = max(ml, r - l + 1)
    
    r += 1

print(ml)