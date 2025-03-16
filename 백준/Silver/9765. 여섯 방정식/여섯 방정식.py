import sys
import math

input = sys.stdin.readline

def solve(c1, c3, c5, c6):
    x2 = math.gcd(c1, c5)
    x1 = c1 // x2
    x3 = c5 // x2
    x6 = math.gcd(c3, c6)
    x7 = c3 // x6
    x5 = c6 // x6

    print(x1, x2, x3, x5, x6, x7)

c1,c2,c3,c4,c5,c6=map(int,input().split())

solve(c1, c3, c5, c6)