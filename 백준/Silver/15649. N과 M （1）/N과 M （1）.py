def go(arr):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    for i in range(1, n+1):
        if i not in arr:
            go(arr+[i])

n, m = map(int,input().split())
go([])