# 1. 소수 판별 -> 에라토스테네스의 체 (그거말고 바로 생각나는게 없었음)
# 2. 종이 조각 붙여서 소수~ -> 순열 만들어야 됨 (itertools permutations)
# 3. 근데 모든 길이에 대해서 해줘야 함 (반복문)


import math
from itertools import permutations

def solution(numbers):
    answer = 0
    unique = set()
    li_num = list(numbers)

    for i in range(1, len(numbers) + 1):
        for perm in permutations(li_num, i):
            num = int(''.join(perm))
            if num not in unique and is_p(num):
                unique.add(num)
                answer += 1

    return answer

def is_p(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True