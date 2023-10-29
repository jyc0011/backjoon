import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    li = sys.stdin.readline().rstrip()
    max_depth = 0
    depth = 0
    for i in li:
        if i == '[':
            depth += 1
            max_depth = max(depth, max_depth)
        elif i == ']':
            if depth > 0:
                depth -= 1
    print(2**max_depth)