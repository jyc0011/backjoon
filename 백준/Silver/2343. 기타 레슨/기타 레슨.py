import sys

def required_blu_rays(lectures, max_length):
    # 각 블루레이의 최대 길이 'max_length'로 주어질 때
    # 필요한 블루레이의 수를 계산
    count = 1  # 최소 한 개의 블루레이는 항상 필요
    current_length = 0

    for lecture in lectures:
        # 현재 블루레이에 더 이상 강의를 추가할 수 없으면 새로운 블루레이 필요
        if current_length + lecture > max_length:
            count += 1
            current_length = 0
        current_length += lecture

    return count

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lectures = list(map(int, input().rstrip().split()))

min_length, max_length = max(lectures), sum(lectures)

while min_length <= max_length:
    potential_length = (min_length + max_length) // 2
    
    # 'potential_length'로 주어진 길이로 필요한 블루레이 수를 확인
    if required_blu_rays(lectures, potential_length) > m:
        min_length = potential_length + 1
    else:
        max_length = potential_length - 1

print(min_length)