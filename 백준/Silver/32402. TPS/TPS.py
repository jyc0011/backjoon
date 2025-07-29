import sys
input = sys.stdin.readline

xp, yp = 0, 0
ox, oy = 0, -1

move_map = {'W': lambda ox, oy: (-ox, -oy),
    'S': lambda ox, oy: ( ox,  oy),
    'A': lambda ox, oy: ( oy, -ox),
    'D': lambda ox, oy: (-oy,  ox)}

n = int(input())

for _ in range(n):
    cmd = input().strip()
    if cmd == 'MR':
        ox, oy =  oy, -ox
    elif cmd == 'ML':
        ox, oy = -oy,  ox
    else:
        dx, dy = move_map[cmd](ox, oy)
        xp += dx
        yp += dy
    xc, yc = xp + ox, yp + oy
    print(xp ,yp, xc, yc)