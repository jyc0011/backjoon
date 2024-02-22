import sys

input=sys.stdin.readline

def LIS(nums):
    lis = []
    for num in nums:
        if not lis or num > lis[-1]:
            lis.append(num)
        else:
            min_, max_ = 0, len(lis) - 1
            while min_ < max_:
                mid = (min_ + max_) // 2
                if lis[mid] < num:
                    min_ = mid + 1
                else:
                    max_ = mid
            lis[min_] = num
    return len(lis)

N = int(input())
A = list(map(int,input().rstrip().split()))

print(LIS(A))