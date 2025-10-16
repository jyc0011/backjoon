import sys
input = sys.stdin.readline
N = int(input())
S = input().strip()
MOD = 10**9 + 7
r = 0
ro = 0
roc = 0
rock = 0
power = 1

for i in range(N):
    char = S[i]
    if char == 'R':
        r = (r + power) % MOD
    elif char == 'O':
        ro = (ro + r) % MOD
    elif char == 'C':
        roc = (roc + ro) % MOD
    elif char == 'K':
        rock = (rock + roc) % MOD
    power = (power * 2) % MOD
print(rock)