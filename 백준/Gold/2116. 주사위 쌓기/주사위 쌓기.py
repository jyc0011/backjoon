import sys

input = sys.stdin.readline

def func(bottom, dice):
    for i in range(6):
        if dice[i] == bottom:
            index = i
            break
    if index == 0:
        return dice[5], max(dice[1], dice[2], dice[3], dice[4])
    elif index == 1:
        return dice[3], max(dice[0], dice[2], dice[4], dice[5])
    elif index == 2:
        return dice[4], max(dice[0], dice[1], dice[3], dice[5])
    elif index == 3:
        return dice[1], max(dice[0], dice[2], dice[4], dice[5])
    elif index == 4:
        return dice[2], max(dice[0], dice[1], dice[3], dice[5])
    elif index ==5:
        return dice[0], max(dice[1], dice[2], dice[3], dice[4])

N = int(input())
dices = [list(map(int, input().rstrip().split())) for _ in range(N)]

ans = 0
for i in range(1, 7):
    start = i
    s_sum = 0
    for j in range(0, N):
        start, side = func(start, dices[j])
        s_sum += side
    if ans < s_sum:
        ans = s_sum

print(ans)