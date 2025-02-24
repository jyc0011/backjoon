def calc(a, b, op): # 연산 결과 축약
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
        
def dfs(start, end, dp_max, dp_min, arr): 
    if start == end: # 시작과 끝이 같다는건 계산이 끝났다는 의미
        return int(arr[start]), int(arr[start])
    if dp_max[start][end] is not None: # 이미 계산한적이 있음(메모이제이션)
        return dp_max[start][end], dp_min[start][end]
    max_val = float('-inf')
    min_val = float('inf')
    for i in range(start + 1, end, 2): # 연산자 기준으로 분할정복
        op = arr[i]
        left_max, left_min = dfs(start, i - 1, dp_max, dp_min, arr) # 연산자 기준 좌측 범위 최댓값, 최솟값
        right_max, right_min = dfs(i + 1, end, dp_max, dp_min, arr) # 연산자 기준 우측 범위 최댓값, 최솟값
        max_val = max(max_val, 
                    calc(left_max, right_max, op),
                    calc(left_min, right_min, op),
                    calc(left_max, right_min, op),
                    calc(left_min, right_max, op)) # 각 방식 중 최댓값을 구함
        min_val = min(min_val, 
                    calc(left_max, right_max, op),
                    calc(left_min, right_min, op),
                    calc(left_max, right_min, op),
                    calc(left_min, right_max, op)) # 각 방식 중 최솟값을 구함
        dp_max[start][end] = max_val # 저장 (메모이제이션)
        dp_min[start][end] = min_val # 저장 (메모이제이션)
    return max_val, min_val
    
def solution(arr):
    n = len(arr)
    dp_max = [[None] * n for _ in range(n)]
    dp_min = [[None] * n for _ in range(n)]
    max_result, _ = dfs(0, n - 1, dp_max, dp_min, arr)
    answer = max_result
    return answer