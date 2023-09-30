n, x = map(int, input().rstrip().split())
day = list(map(int, input().rstrip().split()))

result = sum(day[:x])
cnt = 1
prev_sum = result

for start in range(1, n - x + 1):
    curr_sum = prev_sum - day[start - 1] + day[start + x - 1]
    if curr_sum > result:
        result = curr_sum
        cnt = 1
    elif curr_sum == result:
        cnt += 1
    
    prev_sum = curr_sum

if result == 0:
    print("SAD")
else:
    print(result)
    print(cnt)
