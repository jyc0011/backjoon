import sys

input = sys.stdin.readline

N = int(input())
b = []
for _ in range(N):
    b.append(list(map(int, input().split())))

def solve(x):
    s = {}
    for r in range(N):
        for c in range(N):
            if (r + c) % 2 == x and b[r][c] == 1:
                sId = r - c
                bId = r + c
                
                if sId not in s:
                    s[sId] = []
                s[sId].append(bId)

    temp = list(s.keys())
    visited = [False] * (2 * N) 
    
    def backtrack(idx):
        if idx == len(temp):
            return 0
        id = temp[idx]
        skip = backtrack(idx + 1)
        place = 0
        for bId in s[id]:
            if not visited[bId]:
                visited[bId] = True 
                place = max(place, 1 + backtrack(idx + 1))
                visited[bId] = False 
        return max(skip, place)
    return backtrack(0)

ans_white = solve(0)
ans_black = solve(1)
print(ans_white + ans_black)