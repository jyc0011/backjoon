import sys

input=sys.stdin.readline

def LIS(nums):
    temp = []
    prev = [-1] * len(nums)
    idx_map = [-1] * len(nums)

    for i, num in enumerate(nums):
        left, right = 0, len(temp)
        while left < right:
            mid = (left + right) // 2
            if temp[mid] < num:
                left = mid + 1
            else:
                right = mid
        if left == len(temp):
            temp.append(num)
        else:
            temp[left] = num
        if left > 0:
            prev[i] = idx_map[left-1]
        idx_map[left] = i

    lis_len = len(temp)
    lis_seq = []
    last_idx = idx_map[lis_len-1]
    while last_idx != -1:
        lis_seq.append(nums[last_idx])
        last_idx = prev[last_idx]
    lis_seq.reverse()

    return lis_len, lis_seq

N = int(input())
A = list(map(int,input().rstrip().split()))

l, s = LIS(A)

print(l)
print(*s)