import sys
from collections import deque

def win_check(ground):
    if ground[0] and ground[0][0] == 5:
        return 0
    if ground[1] and ground[1][0] == 5:
        return 0
    if ground[0] and ground[1] and ground[0][0] + ground[1][0] == 5:
        return 1
    return -1

input = sys.stdin.readline
N, M = map(int, input().split())
deck = [deque(), deque()]
ground = [deque(), deque()]

for _ in range(N):
    a, b = map(int, input().split())
    deck[0].appendleft(a)
    deck[1].appendleft(b)

turn = 0
for _ in range(M):
    ground[turn].appendleft(deck[turn].popleft())
    if not deck[turn]:
        print('do' if turn else 'su')
        sys.exit()
    w = win_check(ground)
    if w != -1:
        l = 1 - w
        while ground[l]:
            deck[w].append(ground[l].pop())
        while ground[w]:
            deck[w].append(ground[w].pop())
    turn = 1 - turn

if len(deck[0]) > len(deck[1]):
    print('do')
elif len(deck[0]) < len(deck[1]):
    print('su')
else:
    print('dosu')