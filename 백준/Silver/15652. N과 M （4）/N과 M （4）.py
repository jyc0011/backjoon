n,m = list(map(int,input().split()))
s = []
def go(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        s.append(i)
        go(i)
        s.pop()
go(1)