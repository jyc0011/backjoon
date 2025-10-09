import re

def level1(id):
    return id.lower()

def level2(id):
    return re.sub(r'[^a-z0-9\-_.]', '', id)

def level3(id):        
    return re.sub(r'\.{2,}', '.', id)

def level4(id):
    return id.strip('.')

def level5(id):
    if not id:
        return 'a'
    return id

def level6(id):
    if len(id) >= 16:
        id = id[:15]
        if id.endswith('.'):
            id = id[:-1]
    return id

def level7(id):
    num=len(id)
    last=id[-1]
    while num < 3:
        id+=last
        num+=1
    return id

def solution(new_id):
    answer = level1(new_id)
    answer = level2(answer)
    answer = level3(answer)
    answer = level4(answer)
    answer = level5(answer)
    answer = level6(answer)
    answer = level7(answer)
    return answer