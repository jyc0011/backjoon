import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    
    arranged = [0] * N
    left, right = 0, N - 1
    for i in range(N):
        if i % 2 == 0:
            arranged[left] = logs[i]
            left += 1
        else:
            arranged[right] = logs[i]
            right -= 1

    max_diff = 0
    for i in range(N):
        diff = abs(arranged[i] - arranged[(i + 1) % N])
        max_diff = max(max_diff, diff)

    print(max_diff)