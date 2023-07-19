n=int(input())
a=list(input())
score=0
for i in range(n):
    score+=(ord(a[i])-64)
    
print(score)