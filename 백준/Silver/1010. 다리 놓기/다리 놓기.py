import math

t = int(input())
results = []

for _ in range(t):
    n, m = map(int, input().split())
    results.append(math.comb(m, n))

# 결과 출력
for result in results:
    print(result)