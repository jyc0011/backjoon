a,b=map(int, input().split())
m=1
for i in range(a,b+1):
    m*=i*(1+i)//2
print(m%14579)