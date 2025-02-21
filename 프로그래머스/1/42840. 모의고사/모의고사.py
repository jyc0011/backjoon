def solution(answers):
    check = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    score = [0, 0, 0]
    
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == check[j][i % len(check[j])]:
                score[j] += 1

    max_score = max(score)
    answer = [i + 1 for i in range(3) if score[i] == max_score]
    
    return answer
