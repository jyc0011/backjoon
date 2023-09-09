import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
broken = set(map(int, input().split()))

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - target)

# 0부터 1000000까지 순회하며 계산
for nums in range(1000001):
    nums_str = str(nums)
    
    # 현재 숫자에 고장난 숫자가 포함되어 있으면 넘어감
    if any(int(digit) in broken for digit in nums_str):
        continue

    # 고장난 숫자가 없는 경우, min_count 비교 후 업데이트
    min_count = min(min_count, abs(nums - target) + len(nums_str))

print(min_count)
