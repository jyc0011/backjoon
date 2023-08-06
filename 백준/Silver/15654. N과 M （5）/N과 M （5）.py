def go():
    if len(out) == m:
        print(' '.join(map(str,out)))
        return
    for i in range(n):
        if not visited[i]:
            out.append(l[i])
            visited[i]=True
            go()
            visited[i]=False
            out.pop()

n, m = map(int,input().split())
l=list(map(int,input().split()))
l.sort()
visited = [False] * n
out=[]
go()