import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n = int(input())
    if n == 0:
        return False
    rules = []
    for _ in range(n):
        rules.append(input().split())
    startStr = input().rstrip()
    endStr = input().rstrip()
    targetLen = len(endStr)
    queue = deque([(startStr, 0)])
    visited = {startStr}
    while queue:
        currentStr, steps = queue.popleft()
        if currentStr == endStr:
            print(steps)
            return True
        if len(currentStr) >= targetLen:
            continue
        for alpha, beta in rules:
            nextStr = currentStr.replace(alpha, beta)
            if nextStr not in visited and len(nextStr) <= targetLen:
                visited.add(nextStr)
                queue.append((nextStr, steps + 1))
    print("-1")
    return True

while solve():
    pass