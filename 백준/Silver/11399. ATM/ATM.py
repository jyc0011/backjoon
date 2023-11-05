N = int(input())
P = list(map(int, input().split()))
P.sort()
total = 0
for i in range(N):
    total += P[i] * (N - i)
print(total)