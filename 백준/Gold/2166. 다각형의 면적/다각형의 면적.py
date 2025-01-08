import sys

def calc(N, num):
    temp1=num[N-1][0]*num[0][1]
    temp2=num[0][0]*num[N-1][1]
    for i in range(0, N-1):
        temp1+=num[i][0]*num[i+1][1]
        temp2+=num[i+1][0]*num[i][1]
    return abs(temp1-temp2)/2

N=int(input())
num = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(f"{calc(N, num):.1f}")