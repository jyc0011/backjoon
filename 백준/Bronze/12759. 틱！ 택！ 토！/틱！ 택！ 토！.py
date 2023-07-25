tick_tack = [[0,0,0] for _ in range(3)]

if int(input()) == 1:
    player1 = 1
    player2 = 2
else:
    player1 = 2
    player2 = 1

def check_win(board, player):
    for i in range(3):
        if board[i] == [player]*3: return True
        if [row[i] for row in board] == [player]*3: return True  
    if [board[i][i] for i in range(3)] == [player]*3: return True 
    if [board[i][2-i] for i in range(3)] == [player]*3: return True
    return False

for i in range(9):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if i % 2 == 0:
        tick_tack[x][y] = player1
        if check_win(tick_tack, player1):
            print(player1)
            break
    else:
        tick_tack[x][y] = player2
        if check_win(tick_tack, player2):
            print(player2)
            break
else:
    print(0)
