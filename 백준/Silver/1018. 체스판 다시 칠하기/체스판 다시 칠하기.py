N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

min_changes = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        changes_1 = 0
        changes_2 = 0
        for k in range(8):
            for l in range(8):
                if (board[i+k][j+l] != 'W') == (k%2 == l%2): changes_1 += 1
                if (board[i+k][j+l] != 'B') == (k%2 == l%2): changes_2 += 1
        min_changes = min(min_changes, changes_1, changes_2)

print(min_changes)
