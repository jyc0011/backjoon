from collections import deque

def solution(progresses, speeds):
    answer = []
    day = deque()

    for i in range(len(speeds)):
        remain = (100 - progresses[i])
        if remain % speeds[i] == 0:
            day.append(remain // speeds[i])
        else:
            day.append((remain // speeds[i]) + 1)

    while day:
        current = day.popleft()
        count = 1
        while day and day[0] <= current:
            day.popleft()
            count += 1
        answer.append(count)
        
    return answer