import sys

def find(s):
    n = len(s)
    T = sum(s)
    largest = max(range(n), key=lambda i: s[i])
    M = s[largest]

    if M > T - M:
        return "impossible"

    rooms = [i for i in range(n) if i != largest]
    rooms.sort(key=lambda i: s[i], reverse=True)

    order = [largest + 1] + [r + 1 for r in rooms]
    return order


n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().rstrip().split()))
result = find(s)

if isinstance(result, list):
    print(" ".join(map(str, result)))
else:
    print(result)