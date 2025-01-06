import sys

def calc(s, n, li):
    ans = []
    for l, r, t in li: # l->시작, r-> 끝, t-> 포함되어야 하는 문자열
        temp = s[l-1:r]
        if t in temp:
            ans.append("+")
        else:
            ans.append("-")
    return "".join(ans)

s = input().rstrip() # 암호문
n = int(input().rstrip())
li = [] # l, r, t

for _ in range(n):
    lrt = sys.stdin.readline().rstrip().split()
    li.append(tuple(map(int, lrt[:2])) + (lrt[2],))

print(calc(s, n, li))