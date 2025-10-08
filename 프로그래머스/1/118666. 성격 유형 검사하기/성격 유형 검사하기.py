def calc(a,b,li):
    if li[a] >= li[b]:
        return a
    else:
        return b

def solution(survey, choices):
    answer = ''
    li = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        if c < 4:
            score = 4 - c
            li[s[0]] += score
        elif c > 4:
            score = c - 4
            li[s[1]] += score
    answer += calc('R','T', li)
    answer += calc('C','F', li)
    answer += calc('J','M', li)
    answer += calc('A','N', li)
    return answer