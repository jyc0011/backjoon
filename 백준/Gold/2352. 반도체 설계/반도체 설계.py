import sys
import bisect

input=sys.stdin.readline

def calc(port):
    sub = []
    for p in port:
        idx = bisect.bisect_left(sub, p)
        if idx == len(sub):
            sub.append(p)
        else:
            sub[idx] = p
    return len(sub)


n = int(input())
port = list(map(int, input().split()))

print(calc(port))