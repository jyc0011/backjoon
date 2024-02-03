import sys

input=sys.stdin.readline

def max_sub(X):
    max_s = X[0]
    c_max = X[0]
    
    for x in X[1:]:
        c_max = max(x, c_max + x)
        max_s = max(max_s, c_max)
    
    return max_s

T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    print(max_sub(X))