import sys

input = sys.stdin.readline

def dfs(nowW, nowE):
    global maxE
    if len(nowW) == 2:
        maxE = max(maxE, nowE)
        return
    for i in range(1, len(nowW) - 1):
        addE = nowW[i-1] * nowW[i+1]
        temp = nowW[:i] + nowW[i+1:]
        dfs(temp, nowE + addE)

n = int(input())
w = list(map(int, input().split()))
maxE = 0
dfs(w, 0)
print(maxE)