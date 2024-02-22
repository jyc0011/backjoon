import sys
from collections import deque

n=int(input())

b=list(map(int,sys.stdin.readline().rstrip().split()))
order=[]
balloon=deque([(i+1,b[i]) for i in range(n)])

while balloon:
    idx, move = balloon.popleft()
    order.append(idx)
    
    if move > 0:
        balloon.rotate(-(move - 1))
    else:
        balloon.rotate(-move)
        
print(*order)