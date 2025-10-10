directions={'d':(1,0),'l':(0,-1),'r':(0,1),'u':(-1,0)}

def solution(n, m, x, y, r, c, k):
    answer = ''
    check=abs(r-x)+abs(c-y)
    if (check-k)%2 == 1 or check > k:
        return 'impossible'
        
    nowX,nowY=x,y
    for _ in range(k):
        for move in "dlru":
            dX,dY=directions[move]
            nextX,nextY=nowX+dX,nowY+dY
            if 0<nextX<n+1 and 0<nextY<m+1:
                movingCnt=k-len(answer)-1
                distance=abs(nextX-r)+abs(nextY-c)
                if movingCnt >=distance and (movingCnt-distance)%2==0:
                    answer+=move
                    nowX,nowY=nextX,nextY
                    break
    return answer