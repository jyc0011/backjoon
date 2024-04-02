from itertools import combinations
from collections import defaultdict

def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for information in info:
        information = information.split()
        conditions = information[:-1]
        score = int(information[-1])
        for i in range(5):
            for combination in combinations(range(4), i):
                temp_conditions = conditions.copy()
                for index in combination:
                    temp_conditions[index] = "-"
                key = ''.join(temp_conditions)
                dic[key].append(score)
    for scores in dic.values():
        scores.sort()
    
    for q in query:
        q = q.replace("and ", "").split()
        query_key = ''.join(q[:-1])
        query_score = int(q[-1])
        if query_key in dic:
            scores_list = dic[query_key]
            idx = binary_search(scores_list, query_score)
            answer.append(len(scores_list) - idx)
        else:
            answer.append(0)
    return answer