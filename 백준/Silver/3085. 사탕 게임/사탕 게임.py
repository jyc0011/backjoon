import sys
import heapq

input = sys.stdin.readline

def cnt_max(board, N):
    max_ = 1
    for i in range(N):
        row_count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                row_count += 1
                max_ = max(max_, row_count)
            else:
                row_count = 1
        col_count = 1
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                col_count += 1
                max_ = max(max_, col_count)
            else:
                col_count = 1
    return max_

N=int(input())
board=[list(input().rstrip()) for _ in range(N)]
ans=0

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, cnt_max(board, N))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i + 1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            ans = max(ans, cnt_max(board, N))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j] 

print(ans)