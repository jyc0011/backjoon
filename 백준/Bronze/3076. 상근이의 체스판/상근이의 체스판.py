# 완전탐색

import sys
input = sys.stdin.readline

R,C=map(int,input().split())
A,B=map(int,input().split())

# 가장 왼쪽은 검정색이다.
# R개 | C개 -> A*B
li=[]
opposite=[]
for i in range(C):
    if i%2==0:
        for _ in range(B):
            li.append("X")
            opposite.append(".")
    else:
        for _ in range(B):
            li.append(".")
            opposite.append("X")
            

for i in range(R):
    if i%2==0:
        for _ in range(A):
            print("".join(li))
    else:
        for _ in range(A):
            print("".join(opposite))
