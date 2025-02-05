import sys

input = sys.stdin.readline().rstrip()

def precedence(op):
    if op == '(':
        return 0
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    return -1

stack = []
result = []

for ch in input:
    if ch.isalpha():
        result.append(ch)
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and precedence(stack[-1]) >= precedence(ch):
            if stack[-1] == '(':
                break
            result.append(stack.pop())
        stack.append(ch)

while stack:
    result.append(stack.pop())
print("".join(result))