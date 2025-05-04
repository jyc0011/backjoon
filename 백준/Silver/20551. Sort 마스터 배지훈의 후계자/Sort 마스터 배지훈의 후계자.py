import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = sorted(A)
first_pos = {}
for idx, val in enumerate(B):
    if val not in first_pos:
        first_pos[val] = idx
out_lines = []
for _ in range(M):
    d = int(input())
    out_lines.append(str(first_pos.get(d, -1)))
print('\n'.join(out_lines))