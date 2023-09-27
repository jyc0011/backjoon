import sys

input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
lectures=list(map(int,input().rstrip().split()))

start, end = max(lectures), sum(lectures)

while start <= end:
    mid = (start + end) // 2
    # 최대 길이가 'mid'인 경우
    count = 1 
    total_length = 0  # 현재 Blu-ray의 총 강의 길이
    
    for lecture in lectures:
        if total_length + lecture > mid:
            count += 1
            total_length = 0
        total_length += lecture
    
    # M개 이상의 Blu-ray가 필요한 경우 크기 늘리기
    if count > m:
        start = mid + 1
    # 그렇지 않으면 크기 감소
    else:
        end = mid - 1

print(start)