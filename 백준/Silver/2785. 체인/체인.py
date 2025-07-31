n = int(input())
li = list(map(int, input().split()))
li.sort()
need = n - 1
ans = 0
for i in range(n):
    if need == 0:
        break       
    now = li[i]
    if now >= need:
        ans += need
        need = 0
    else:
        ans += now
        need -= now + 1 

print(ans)