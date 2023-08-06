import sys
N = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
cnt = list(map(int,sys.stdin.readline().split()))
max_ans = -1000000000
min_ans = 1000000000

def dfs(idx, ans):
    global max_ans,min_ans
    
    if idx == N:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return
    
    if cnt[0] > 0:
        cnt[0] -= 1
        dfs(idx+1, ans+a[idx])
        cnt[0] += 1
    if cnt[1] > 0:
        cnt[1] -= 1
        dfs(idx+1, ans-a[idx])
        cnt[1] += 1
    if cnt[2] > 0:
        cnt[2] -= 1
        dfs(idx+1, ans*a[idx])
        cnt[2] += 1
    if cnt[3] > 0:
        cnt[3] -= 1
        dfs(idx+1, int(ans/a[idx]))
        cnt[3] += 1
        
dfs(1,a[0])
print(max_ans)
print(min_ans)