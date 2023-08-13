import sys

def is_pass(x, y, op):
    if op == '<':
        if x > y:
            return False
    if op == '>':
        if x < y:
            return False
    return True

def find_extreme_numbers(index, num):
    if index == n + 1:
        extremes.append(num)
        return

    for i in range(10):
        if i in used: continue

        if index == 0 or is_pass(num[index - 1], str(i), symbols[index - 1]):
            used.add(i)
            find_extreme_numbers(index + 1, num + str(i))
            used.remove(i)

n = int(sys.stdin.readline())
symbols = sys.stdin.readline().split()

extremes = []
used = set()

find_extreme_numbers(0, '')

extremes.sort()
print(extremes[-1])  # 최댓값
print(extremes[0])   # 최솟값
