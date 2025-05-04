import sys
input = sys.stdin.readline

N = int(input())
unwashed = list(range(N, 0, -1))
wet = []
clean = []

for line in sys.stdin:
    if not line.strip():
        continu
    cmd, d = map(int, line.split())
    if cmd == 1:
        for _ in range(d):
            wet.append(unwashed.pop())
    else:
        for _ in range(d):
            clean.append(wet.pop())
for dish in reversed(clean):
    print(dish)