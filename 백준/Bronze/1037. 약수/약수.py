# 정렬을 이용하면 어떻게 달라지는가?
cnt=int(input())
n=sorted(list(map(int, input().split())))
print(n[0]*n[-1])