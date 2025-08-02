from collections import deque

def solution(players, m, k):
    answer = 0
    serverQ=deque([])
    for _ in range(k):
        serverQ.append(0)
    nowS=0
    
    for i in range(24):
        temp=players[i]//m
        nowS-=serverQ.popleft()
        if temp - nowS > 0 :
            answer+=(temp-nowS)
            serverQ.append(temp-nowS)
            nowS=temp
        else :
            serverQ.append(0)
    return answer