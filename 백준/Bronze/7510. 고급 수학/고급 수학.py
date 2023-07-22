n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    a.sort()  # 가장 긴 변이 마지막에 오도록 정렬
    if a[0]**2 + a[1]**2 == a[2]**2:
        print(f'Scenario #{i+1}:\nyes\n')
    else:
        print(f'Scenario #{i+1}:\nno\n')
