import sys

li=[int(sys.stdin.readline()) for _ in range(9)]
total=sum(li)
    
for i in range(8):
    for j in range(i+1,9):
        if total-li[i]-li[j]==100:
            x,y=i,j
            break
li.pop(y)
li.pop(x)
for k in li:
    print(k)