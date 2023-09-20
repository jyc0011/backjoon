import math

n = int(input())

prime= []

# 에라토스테네스의 체
a = [False,False] + [True]*(n-1)
for i in range(2,int(n**0.5)+1):
    if a[i]:
        a[i*2::i] = [False]*((n-i)//i)
        
for i in range(n+1):
    if a[i] == True:
        prime.append(i)
        
c,s = 0,0
l,r = 0,0
while(True):
    if s == n:
        c+=1
    if s > n:
        s -= prime[l]
        l+=1
    elif r == len(prime):
        break
    else:
        s += prime[r]
        r+=1
        
print(c)