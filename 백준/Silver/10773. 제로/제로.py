import sys

k=int(sys.stdin.readline())
li=[]
for i in range(k):
    a=int(sys.stdin.readline())
    if a==0:
        if li:
            li.pop()
    else:
        li.append(a)
print(sum(li))