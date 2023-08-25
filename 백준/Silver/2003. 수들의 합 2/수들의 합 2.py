import sys

n,m=map(int,sys.stdin.readline().split())
li=list(map(int, sys.stdin.readline().split()))

left, right=0, 1
# 투포인터. 여기left->##<-여기right ####

ans = 0
# 최초 결과

while right <= n and left<=right: 
    current_sum = sum(li[left:right])
    
    if current_sum == m:  # 내가 찾고자 하는 값이 m과 같으먼
        ans += 1
        right += 1  # right 값을 증가
    elif current_sum < m:  # 작아도 right 값을 증가
        right += 1
    else:  # 클 경우
        left += 1  # left 값을 증가

print(ans)