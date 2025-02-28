import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())

st = (X + Y) * W  

df = min(X, Y) * S + abs(X - Y) * W  
if (X + Y) % 2 == 0:
    dp = max(X, Y) * S
else:
    dp = (max(X, Y) - 1) * S + W
    
print(min(st, df, dp))