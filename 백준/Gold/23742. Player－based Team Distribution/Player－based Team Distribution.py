import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
S = 0
V = 0
reject = 0
for a in A:
    if a > 0:
        S += 1
        V += a
    else:
        if (S * a + V) > 0:
            S += 1
            V += a
        else:
            reject += a
ans = S * V + reject
print(ans)