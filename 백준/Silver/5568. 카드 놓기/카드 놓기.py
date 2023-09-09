from itertools import permutations
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = [sys.stdin.readline().strip() for _ in range(n)]

combos = permutations(cards, k)

numbers = set()
for combo in combos:
    numbers.add(''.join(combo))

print(len(numbers))
