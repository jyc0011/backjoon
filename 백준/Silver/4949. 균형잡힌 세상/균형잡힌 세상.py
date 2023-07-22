import sys
import re

while True:
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    s = re.sub('[^()\[\]]', '', s)
    stack = []
    for c in s:
        if c in "([":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
    else:
        print("yes" if not stack else "no")
