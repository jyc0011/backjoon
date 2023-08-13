import sys
from collections import Counter

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li = sorted(list(map(int, sys.stdin.readline().split())))
    ans = 0
    counter = Counter(li)
    
    for i in range(n-1):
        for j in range(i+1, n):
            first = li[i]
            second = li[j]
            third = 2 * second - first
            if third in counter:
                ans += 1
    
    print(ans)
