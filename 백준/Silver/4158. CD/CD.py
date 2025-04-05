import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    cd_sang = [int(input()) for _ in range(N)]
    cd_sun = [int(input()) for _ in range(M)]

    cnt = 0
    i = j = 0

    while i < N and j < M:
        if cd_sang[i] == cd_sun[j]:
            cnt += 1
            i += 1
            j += 1
        elif cd_sang[i] < cd_sun[j]:
            i += 1
        else:
            j += 1

    print(cnt)