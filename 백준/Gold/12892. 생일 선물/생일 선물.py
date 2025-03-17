import sys
input = sys.stdin.readline

N, D = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

gifts.sort(key=lambda x: x[0])

ans = 0
sum_ = 0
l = 0

for r in range(N):
    P, V = gifts[r]
    sum_ += V
    while P - gifts[l][0] >= D:
        sum_ -= gifts[l][1]
        l += 1
    ans = max(ans, sum_)

print(ans)