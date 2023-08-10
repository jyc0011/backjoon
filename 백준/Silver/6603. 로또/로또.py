import itertools
import sys

while True:
    array = list(map(int, sys.stdin.readline().split()))
    k = array[0]
    S = array[1:]
    for i in itertools.combinations(S, 6):
        print(*i)
    if k == 0:
        exit()
    print()