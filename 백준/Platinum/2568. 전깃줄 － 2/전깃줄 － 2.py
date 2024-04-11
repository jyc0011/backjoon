import sys
from bisect import bisect_left

def find_LIS(E):
    LIS = []
    track = [-1] * len(E)
    for i in range(len(E)):
        if len(LIS) == 0 or E[LIS[-1]][1] < E[i][1]:
            if len(LIS) > 0: track[i] = LIS[-1]
            LIS.append(i)
        else:
            pos = bisect_left([E[j][1] for j in LIS], E[i][1])
            if pos > 0: track[i] = LIS[pos-1]
            LIS[pos] = i
    return LIS, track

def find(track, end_pos):
    removed = set(range(len(track)))
    pos = end_pos
    while pos != -1:
        removed.remove(pos)
        pos = track[pos]
    return sorted([E[i][0] for i in removed])

input = sys.stdin.readline
n = int(input())
E = list(list(map(int,input().rstrip().split())) for _ in range(n))
E.sort(key=lambda x:x[0])

LIS, track = find_LIS(E)
removed_lines = find(track, LIS[-1])

print(len(removed_lines))
for line in removed_lines:
    print(line)