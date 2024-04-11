ans=[0 for _ in range(10)]
N=input()
digit=len(N)
for x in N:
    digit-=1
    for i in range(int(x)):
        ans[i]+= 10 ** digit
        for j in range(10):
            if digit>=1:
                ans[j]+= (10 ** (digit - 1)) * digit
    ans[0]-= 10 ** digit
    if digit:
        ans[int(x)]+=(int(''.join(N[-digit:])) + 1)
    else:
        ans[int(x)]+=1
print(*ans)