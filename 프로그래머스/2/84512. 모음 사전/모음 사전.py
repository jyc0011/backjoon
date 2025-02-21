def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]

    for i, w in enumerate(word):
        idx = alpha.index(w)
        answer += idx * weights[i] + 1

    return answer
