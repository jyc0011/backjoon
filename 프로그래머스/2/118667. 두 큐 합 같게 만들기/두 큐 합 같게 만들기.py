from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum_,sumQ1=0,0
    num=0
    q1,q2=deque(),deque()
    for i in queue1:
        q1.append(i)
        sum_+=i
        num+=1
        sumQ1+=i
    for j in queue2:
        q2.append(j)
        sum_+=j
        num+=1
    if sum_%2 == 1:
        return -1
    sum_//=2
    num*=4
    while sumQ1!=sum_:
        if answer >= num:
            return -1
        if sumQ1 >sum_:
            a=q1.popleft()
            q2.append(a)
            sumQ1-=a
        else:
            a=q2.popleft()
            q1.append(a)
            sumQ1+=a
        answer+=1
    return answer