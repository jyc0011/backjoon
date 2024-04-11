import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
sharks = {}

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r - 1, c - 1)] = [s, d, z]

def move_sharks():
    new_sharks = {}
    for (r, c), (s, d, z) in sharks.items():
        nr, nc = r, c
        speed = s
        if d <= 2:
            speed %= ((R - 1) * 2)
            for _ in range(speed):
                if d == 1 and nr == 0:
                    d = 2
                elif d == 2 and nr == R - 1:
                    d = 1
                nr += -1 if d == 1 else 1
        else:
            speed %= ((C - 1) * 2)
            for _ in range(speed):
                if d == 4 and nc == 0:
                    d = 3
                elif d == 3 and nc == C - 1:
                    d = 4
                nc += -1 if d == 4 else 1
        if (nr, nc) not in new_sharks or new_sharks[(nr, nc)][2] < z:
            new_sharks[(nr, nc)] = [s, d, z]
    return new_sharks

def catch_shark(king):
    caught_size = 0
    for r in range(R):
        if (r, king) in sharks:
            caught_size = sharks[(r, king)][2]
            del sharks[(r, king)]
            break
    return caught_size

total_size = 0
for fish_king in range(C):
    total_size += catch_shark(fish_king)
    sharks = move_sharks()

print(total_size)