n,m=map(int,input().split())
li=list(map(int,input().split()))
li.sort()

left, right=0, n-1
# 투포인터. 여기left->#####<-여기right

ans = 0
# 최초 결과

while left<right: 
    current_sum = li[left]+li[right]
    if current_sum >= m:  # 내가 고른 값이 m과 같거나 크면
        ans += 1
        right -= 1
        left += 1
    elif current_sum < m:  # 작으면 left증가
        left += 1

print(ans)