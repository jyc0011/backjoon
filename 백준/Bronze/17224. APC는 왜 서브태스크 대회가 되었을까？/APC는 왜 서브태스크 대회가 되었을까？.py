import sys
input = sys.stdin.readline

EASY = 100
HARD = 140

N, L, K = map(int, input().split())
tasks=[tuple(map(int, input().split())) for _ in range(N)]
score = []

for sub1, sub2 in tasks:
    if sub2 <= L:
        score.append(HARD)
    elif sub1 <= L:
        score.append(EASY)

score.sort(reverse=True)

print(sum(score[:K]))