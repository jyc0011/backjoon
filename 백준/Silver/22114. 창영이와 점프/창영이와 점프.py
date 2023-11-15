import sys

input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))
m= 0
s = 0
while m < len(l) - s:
    j = s
    cnt = 0
    jump = False
    while j < len(l):
        if k >= l[j]:
            cnt += 1
        else:
            if jump == True:
                break
            else:
                cnt += 1
                jump = True
        j += 1
    m = max(m, cnt)
    s += 1
    
print(m + 1)