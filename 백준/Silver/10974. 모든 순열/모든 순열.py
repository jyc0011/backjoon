n=int(input())
li=[]

def dfs():
    if len(li)==n:
        print(*li)
        return
    for i in range(1,n+1):
        if i not in li:
            li.append(i)
            dfs()
            li.pop()
dfs()