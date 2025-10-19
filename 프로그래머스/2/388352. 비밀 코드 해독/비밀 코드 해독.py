from itertools import combinations

def cnt(n):
    count = 0
    while n:
        n &= (n - 1)
        count+=1
    return count


def solution(n, q, ans):
    answer = 0
    temp=combinations(range(1, n + 1), 5)
    li=[]
    qBit=[]
    for i in temp:
        mask = 0
        for num in i:
            mask |= (1 << (num - 1))
        li.append(mask)
        
    for i in q:
        mask = 0
        for num in i:
            mask |= (1 << (num - 1))
        qBit.append(mask)
    
    for mask in li:
        flag=True
        for i in range(len(qBit)):
            if cnt(mask&qBit[i])!=ans[i]:
                flag=False
                continue
        if flag:
            answer+=1
        
    return answer