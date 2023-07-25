import sys

n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    score = 0
    for j in range(3):
        if sum(x[j] == a[i][j] for x in a) == 1:
            score += a[i][j]
    print(score)
