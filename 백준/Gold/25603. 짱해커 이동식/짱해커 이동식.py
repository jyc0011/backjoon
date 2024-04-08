import heapq
N, K = map(int, input().split())
cost = list(map(int, input().split()))

# K==1 -> 가장 비용 높은 거로 하면 됨
if K == 1:
    print(max(cost))
#
else:
    ans_li = [] # 구간별 최솟값 저장
    min_idx = 0 # 슬라이딩 윈도우 시작 인덱스

    while min_idx + K <= N: # 슬라이딩 윈도우의 마지막 인덱스가 끝에 도달하지 않음
        slide = cost[min_idx:min_idx + K] # 현재 슬라이딩 윈도우
        min_val = min(slide) # 최소 비용 선택
        min_val_idx = slide.index(min_val) + min_idx # 최소값의 인덱스 찾기
        min_idx = min_val_idx + 1 # 그거 다음부터 확인 (그 앞은 다 min_val이 최소 비용이니까)
        heapq.heappush(ans_li, -min_val)

    print(-heapq.heappop(ans_li))