import sys

input=sys.stdin.readline

def calc(n, d):
    d.sort()
    min_d = float('inf')
    for i in range(n - 3):
        for j in range(i + 3, n):
            s1 = d[i] + d[j]
            l = i + 1
            r = j - 1

            while l < r:
                s2 = d[l] + d[r]
                min_d = min(min_d, abs(s1 - s2))
                
                if s1 > s2:
                    l += 1
                else:
                    r -= 1

    return min_d

n = int(input().strip())
d = list(map(int, input().strip().split()))

print(calc(n, d))