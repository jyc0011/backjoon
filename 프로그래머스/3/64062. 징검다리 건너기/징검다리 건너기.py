def solution(stones, k):
    l, r = 1, max(stones)
    answer = 0
    while l <= r:
        m = (l + r) // 2
        list_zero = 0
        is_possible = True
        for stone in stones:
            if stone < m:  
                list_zero += 1
            else:
                list_zero = 0
            if list_zero >= k:
                is_possible = False
                break
        if is_possible:
            answer = m
            l = m + 1
        else:
            r = m - 1
    return answer