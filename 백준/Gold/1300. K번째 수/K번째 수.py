def find(N, k):
    start, end = 1, N * N

    while start < end:
        mid = (start + end) // 2
        count = sum(min(mid // i, N) for i in range(1, N + 1))
        if count >= k:
            end = mid
        else:
            start = mid + 1

    return start
N=int(input())
k=int(input())
print(find(N, k))