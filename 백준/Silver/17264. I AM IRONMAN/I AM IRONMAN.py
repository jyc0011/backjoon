import sys

n, p = map(int, sys.stdin.readline().rstrip().split())
w, l, g = map(int, sys.stdin.readline().rstrip().split())

info = {}

for _ in range(p):
    name, case = sys.stdin.readline().rstrip().split()
    info[name] = case
    
point = 0
for j in range(n):
    name = sys.stdin.readline().rstrip()

    if info.get(name) == 'W':
        point += w
    else:
        point -= l
        if point < 0:
            point = 0

    if point >= g:
        print("I AM NOT IRONMAN!!")
        sys.exit()

print("I AM IRONMAN!!")