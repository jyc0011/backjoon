def solution(n, w, num):
    answer = 0
    li = [[] for _ in range(w + 1)]
    cur = 1
    layer = 0
    while cur <= n:
        if layer % 2 == 0:
            for i in range(1, w + 1):
                if cur > n:
                    break
                li[i].append(cur)
                cur += 1
        else:
            for i in range(w, 0, -1):
                if cur > n:
                    break
                li[i].append(cur)
                cur += 1
        layer += 1
    
    t = None
    for i in range(1, w + 1):
        if num in li[i]:
            t = i
            break
    while li[t]:
        top = li[t].pop()
        answer += 1
        if top == num:
            break
    return answer