T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    result = 0
    j = 0
    for i in range(N):
        while j < M and A[i] > B[j]:
            j += 1
        result += j
    print(result)