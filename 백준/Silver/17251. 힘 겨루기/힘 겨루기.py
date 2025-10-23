import sys

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
prefixL = [0] * N
prefixL[0] = S[0]
for i in range(1, N):
    prefixL[i] = max(prefixL[i - 1], S[i])
prefixR = [0] * N
prefixR[N - 1] = S[N - 1]
for i in range(N - 2, -1, -1):
    prefixR[i] = max(prefixR[i + 1], S[i])
ansL,ansR = 0, 0
for k in range(N - 1):
    maxL = prefixL[k]
    maxR = prefixR[k + 1]

    if maxL > maxR:
        ansR += 1
    elif maxR > maxL:
        ansL += 1
if ansR > ansL:
    print('R')
elif ansL > ansR:
    print('B')
else:
    print('X')