import sys

input = sys.stdin.readline

line = input().strip()
target = input().strip()
target_len = len(target)
stack = []

for char in line:
    stack.append(char)
    if ''.join(stack[-target_len:]) == target:
        del stack[-target_len:]

if stack:
    print(''.join(stack))
else:
    print("FRULA")