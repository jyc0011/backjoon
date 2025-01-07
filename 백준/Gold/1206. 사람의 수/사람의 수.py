import math
import sys

N = int(input())
scores = []
M=1

for _ in range(N):
    score_str = sys.stdin.readline().rstrip()
    int_p, de_p = score_str.split('.')
    p = int(int_p) * 1000 + int(de_p)
    scores.append(p)
    
while True:
    ans = True
    for p in scores:
        left = math.ceil(p * M / 1000) 
        numerator = (p + 1) * M - 1
        right = numerator // 1000 
        if left > right:
            ans = False
            break
    if ans:
        print(M)
        sys.exit()
    M += 1