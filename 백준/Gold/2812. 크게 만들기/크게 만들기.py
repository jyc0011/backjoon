n,k=map(int, input().split())
a=input().strip()
answer = ''
cnt = k

for i in range(n):
    while cnt > 0 and answer and answer[-1] < a[i]:
        answer = answer[:-1]
        cnt -= 1
    answer += a[i] 

if cnt > 0:
    answer = answer[:-cnt]
print(answer)
