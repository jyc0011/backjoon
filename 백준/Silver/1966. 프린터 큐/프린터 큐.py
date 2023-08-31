from collections import deque
import sys

input=sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().rstrip().split())
    importance = list(map(int, input().rstrip().split()))
    
    # (중요도, 인덱스) 튜플 형태로 큐에 저장
    queue = deque([(value, idx) for idx, value in enumerate(importance)])
    counter = 0

    while queue:
        # 현재 문서가 가장 중요한지 확인
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            counter += 1

            # 궁금한 문서가 인쇄되었는지 확인
            if queue[0][1] == M:
                print(counter)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())
