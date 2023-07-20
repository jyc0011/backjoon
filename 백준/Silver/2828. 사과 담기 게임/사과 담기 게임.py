N, M = map(int, input().split())
J = int(input())
apples = [int(input()) for _ in range(J)]

start, end = 1, M
dist = 0

for apple in apples:
    if apple < start:
        dist += start - apple
        start = apple
        end = start + M - 1
    elif apple > end:
        dist += apple - end
        end = apple
        start = end - M + 1
print(dist)
