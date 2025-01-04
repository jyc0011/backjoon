def calc(N):
    start = max(1, N - len(str(N)) * 9)
    for M in range(start, N):
        sum = M
        temp = M
        while temp > 0:
            sum += temp % 10
            temp //= 10
        if sum == N:
            return M
    return 0

N = int(input())
print(calc(N))