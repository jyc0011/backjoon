import sys
li=[]
n=int(sys.stdin.readline())

for i in range(n):
    li.append(sys.stdin.readline().rstrip())
li.sort()    
print(max(li,key=li.count))
