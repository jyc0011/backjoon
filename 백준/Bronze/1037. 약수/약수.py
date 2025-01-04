cnt=int(input())
numbers=list(map(int, input().split()))
min_num, max_num = float('inf'), float('-inf')

for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

n = min_num * max_num
print(n)