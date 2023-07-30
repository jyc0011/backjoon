import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A.sort()
    B.sort()

    result = 0
    j = 0
    for i in range(N):
        while j < M and A[i] > B[j]:
            j += 1
        result += j
    sys.stdout.write(str(result) + "\n")