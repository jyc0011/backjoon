from bisect import bisect_left

N = int(input())
li = list(map(int, input().split()))
li.sort()

answer = 0
for i in range(len(li)-2):
    left, right = i+1, N-1
    while left < right:
        result = li[i]+li[left]+li[right]
        if result > 0:
            right -= 1
        else:
            if result == 0:
                if li[left] == li[right]:
                    answer += right - left
                else:
                    idx = bisect_left(li, li[right])
                    answer += right-idx+1
            left += 1

print(answer)