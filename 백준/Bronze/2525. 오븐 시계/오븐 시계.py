A, B = map(int, input().split())
C = int(input())

total_min = B + C
total_hour = A + total_min // 60
total_hour %= 24
total_min %= 60

print(total_hour, total_min)
