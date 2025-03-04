import sys
input = sys.stdin.readline

def dfs(now, used):
    global ans
    if used >= ans:
        return
    if now == 0: 
        ans = min(ans, used)
        return
    for pos in range(100):
        if (now & (1 << pos)) != 0:
            x, y = divmod(pos, 10)
            break
    for size in range(5, 0, -1):
        if papers[size] == 0:
            continue
        masking = paper_mask[x][y][size]
        if masking == 0:
            continue
        if (now & masking) == masking:
            papers[size] -= 1
            next = now ^ masking
            dfs(next, used + 1)
            papers[size] += 1

field = 0
ans = float('inf')
papers = [0, 5, 5, 5, 5, 5]
paper_mask = [[[0]*6 for _ in range(10)] for __ in range(10)]

for x in range(10):
    row = list(map(int, input().split()))
    for y in range(10):
        if row[y] == 1:
            pos = x * 10 + y
            field |= (1 << pos)
            
for x in range(10):
    for y in range(10):
        pos = x*10 + y
        for size in range(1, 6):
            if x + size > 10 or y + size > 10:
                paper_mask[x][y][size] = 0
                continue
            masking = 0
            for i in range(x, x+size):
                for j in range(y, y+size):
                    masking |= (1 << (i*10 + j))
            paper_mask[x][y][size] = masking

dfs(field, 0)
print(ans if ans != float('inf') else -1)