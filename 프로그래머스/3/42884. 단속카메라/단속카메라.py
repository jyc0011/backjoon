def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    point= -30000
    for a,b in routes:
        if a > point:
            point=b
            answer+=1
    return answer