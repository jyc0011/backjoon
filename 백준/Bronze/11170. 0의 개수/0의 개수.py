import sys
input= sys.stdin.readline
t = int(input())

for _ in range(t):
        N, M = map(int,input().split())
        count_zero = 0
        for num in range(N, M + 1):
            count_zero += str(num).count('0')
        print(count_zero)