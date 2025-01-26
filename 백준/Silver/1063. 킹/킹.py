import sys

input=sys.stdin.readline
d = {"R": (0, 1), "L": (0, -1), "T": (-1, 0), "B": (1, 0),"RT": (-1, 1), "LT": (-1, -1), "RB": (1, 1), "LB": (1, -1)}

def xy(pos):
    return 8 - int(pos[1]), ord(pos[0]) - ord('A')

def calc(coords):
    return chr(coords[1] + ord('A')) + str(8 - coords[0])

king, stone, n = input().rstrip().split()
n = int(n)
commands = [input().rstrip() for _ in range(n)]
kp = xy(king)
sp = xy(stone)
for command in commands:
    dx, dy = d[command]
    nk = (kp[0] + dx, kp[1] + dy)
    if 0 <= nk[0] < 8 and 0 <= nk[1] < 8:
        if nk == sp:
            ns = (sp[0] + dx, sp[1] + dy)
            if 0 <= ns[0] < 8 and 0 <= ns[1] < 8:
                kp = nk
                sp = ns
        else:
            kp = nk
print(calc(kp))
print(calc(sp))