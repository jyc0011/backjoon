import sys
input = sys.stdin.readline

N, M = map(int, input().split())
friends = [[] for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    friends[A].append(B)
    friends[B].append(A)

min_ = float('inf')

for A in range(1, N + 1):
    for B in friends[A]:
        if B > A:
            for C in friends[B]:
                if C > B and C in friends[A]:
                    total = (len(friends[A]) - 2) + (len(friends[B]) - 2) + (len(friends[C]) - 2)
                    min_ = min(min_, total)

if min_ == float('inf'):
    print(-1)
else:
    print(min_)