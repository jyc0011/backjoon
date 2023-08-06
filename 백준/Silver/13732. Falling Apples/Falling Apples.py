import sys
sys.setrecursionlimit(100000)

N,M=map(int, sys.stdin.readline().split())
arr=[]
for i in range(N):
    arr.append(list(input()))
Box=[]
box=[]
for i in range(M):
    for j in range(N):
        if arr[j][i]=='#':
            box.sort()
            Box.append(box)
            box=[]
            box.append(arr[j][i])
            Box.append(box)
            box=[]
        elif j==N-1 :
            box.append(arr[j][i])
            box.sort()
            Box.append(box)
            box=[] 
        else:box.append(arr[j][i])

Box=sum(Box,[])
 
for i in range(N):
    for j in range(M):
        print(Box[N*j+i],end='')
    print()