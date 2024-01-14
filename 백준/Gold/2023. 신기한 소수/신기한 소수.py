def is_p(n): #에라토스테네스의 체
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find(ans):
    global n
    if len(str(ans))==n: #원하는 자릿수면
        if is_p(ans): # 소수인지 확인하고
            print(ans) # 출력
        return
    for i in [1,3,5,7,9]: #아직 원하는 자릿수가 아니면
        temp=ans*10+i
        if is_p(temp):
            find(temp)

n = int(input())
for i in [2,3,5,7]:
    find(i)