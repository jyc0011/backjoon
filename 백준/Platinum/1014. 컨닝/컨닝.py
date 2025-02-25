import sys
input = sys.stdin.readline

def calc(N, M, seats):
    rows = []
    popcount = lambda x: bin(x).count('1')
    for r in range(N):
        valid_masks = []
        for mask in range(1 << M):
            if (mask & (mask << 1)) != 0:
                continue
            can = True
            for c in range(M):
                if (mask & (1 << c)) and seats[r][c] == 1:
                    can = False
                    break
            if not can:
                continue

            valid_masks.append(mask)
        rows.append(valid_masks)
        
    dp = [dict() for _ in range(N)]
    
    for mask in rows[0]:
        dp[0][mask] = popcount(mask)

    for r in range(1, N):
        for mask in rows[r]:
            cnt = popcount(mask)
            for prev, val in dp[r-1].items():
                if ((mask << 1) & prev) == 0 and ((mask >> 1) & prev) == 0:
                    new_val = val + cnt
                    if mask not in dp[r] or dp[r][mask] < new_val:
                        dp[r][mask] = new_val
    return max(dp[N-1].values())

C = int(input())
for _ in range(C):
    N, M = map(int, input().split())
    seats = []
    for _ in range(N):
        line = input().rstrip()
        data = [0 if i == '.' else 1 for i in line]
        seats.append(data)
    print(calc(N, M, seats))