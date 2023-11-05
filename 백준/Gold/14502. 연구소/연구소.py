import copy
from collections import deque
from itertools import combinations
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ch = []
lst_2 = []

dq = deque()

def count(lst):
    cnt = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j]==0:
                cnt +=1
    return cnt

dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 :
            ch.append((i,j))
        if arr[i][j] == 2:
            lst_2.append((i,j))

ans = 0
for i in combinations(ch,3):
    board = copy.deepcopy(arr)
    for x,y in i:
        board[x][y] = 1
    for a,b in lst_2:
        dq.append((a,b))
        while dq:
            now = dq.popleft()
            for k in range(4):
                xx = now[0]+dx[k]
                yy = now[1]+dy[k]
                if 0<=xx<n and 0<=yy<m and board[xx][yy] == 0:
                    board[xx][yy] = 2
                    dq.append((xx,yy))
        
    zero = count(board)
    ans = max(ans,zero)
print(ans)