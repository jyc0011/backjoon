import sys

def toggle(s):
    return 1 if s == 0 else 0

def boy(sw, n):
    for i in range(n-1, len(sw), n):
        sw[i] = toggle(sw[i])
    return sw

def girl(sw, n):
    l, r = n-2, n
    sw[n-1] = toggle(sw[n-1])
    while l >= 0 and r < len(sw):
        if sw[l] == sw[r]:
            sw[l] = toggle(sw[l])
            sw[r] = toggle(sw[r])
            l -= 1
            r += 1
        else:
            break
    return sw

n = int(sys.stdin.readline())
sw = list(map(int, sys.stdin.readline().split()))

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    sw = boy(sw, b) if a == 1 else girl(sw, b)

for i in range(0, len(sw), 20):
    print(*sw[i:i+20])
