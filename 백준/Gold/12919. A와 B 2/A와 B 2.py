import sys

input = sys.stdin.readline

def dfs(s, t):
    global ans
    if ans == 1:
        return
    if t == s:
        ans = 1
        return
    if len(t) < len(s):
        return
    if t.endswith('A'):
        dfs(s, t[:-1])
    if t.startswith('B'):
        dfs(s, t[::-1][:-1])

s=input().rstrip()
t=input().rstrip()
ans=0
# 문자열 뒤에는 A -> A가 뒤에 있음 A를 떼도 됨
# B는 추가하면 뒤집음 -> 반대로 생각하면 B가 앞에 있음 -> B를 떼도됨
# dfs 하자

dfs(s,t)

print(ans)