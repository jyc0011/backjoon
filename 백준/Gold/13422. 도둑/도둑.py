import sys

# 주어진 조건에 따라 도둑이 돈을 훔치는 경우의 수를 반환하는 함수
def solution(houses, N, M, K):
    # 초기 M개의 합 계산
    currentSum = sum(houses[0:M])
    left = 1
    right = M
    
    # 초기 상태에서 k보다 작으면 경우의 수 1 증가
    answer = 1 if currentSum < K else 0

    # 모든 집이 훔친 집의 개수와 같을 때, 바로 결과 반환
    if N == M:
        return answer

    # 슬라이딩 윈도우 방식으로 연속된 M개의 집에 대한 합 갱신
    while left < N:
        # 이전 집의 값을 빼고 다음 집의 값을 더함
        currentSum -= houses[left - 1]
        currentSum += houses[right % N]
        
        # 현재 합이 k보다 작으면 경우의 수 증가
        if currentSum < K:
            answer += 1
        
        left += 1
        right += 1

    return answer

# 테스트 케이스 개수 입력 받기
for _ in range(int(sys.stdin.readline())):
    N, M, K = map(int, sys.stdin.readline().split())
    houses = list(map(int, sys.stdin.readline().split()))
    # 결과 출력
    print(solution(houses, N, M, K))