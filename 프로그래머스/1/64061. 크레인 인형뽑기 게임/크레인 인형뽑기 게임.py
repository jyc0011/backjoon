def solution(board, moves):
    answer = 0
    basket=[]
    num=len(board)
    queue=[[]for _ in range(num)]
    for i in range(num-1,-1,-1):
        for j in range(0,num):
            if board[i][j] !=0:
                queue[j].append(board[i][j])
    for m in moves:
        m-=1
        if queue[m]:
            a=queue[m].pop()
            if basket and basket[-1]==a:
                basket.pop()
                answer+=2
            else:
                basket.append(a)
    return answer