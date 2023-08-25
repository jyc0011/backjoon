import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())

# 고장난 신호등 위치를 -1로 표시하기 위한 초기화
trafficLight = [0] * n
for _ in range(b):
    broken_light = int(input()) - 1
    trafficLight[broken_light] = -1

# 초기 구간(0 ~ k-1)의 고장난 신호등 수를 계산
broken_count = trafficLight[:k].count(-1)

# 최소 고장난 신호등 수를 broken_count로 초기화
min_broken = broken_count

# 투포인터로 나머지 구간 탐색
for i in range(1, n - k + 1):
    # 이전 구간의 첫번째 위치의 신호등이 고장났는지 확인
    if trafficLight[i - 1] == -1:
        broken_count -= 1

    # 새로운 구간의 마지막 위치의 신호등이 고장났는지 확인
    if trafficLight[i + k - 1] == -1:
        broken_count += 1

    # 최소 고장난 신호등 수 업데이트
    min_broken = min(min_broken, broken_count)

print(min_broken)
