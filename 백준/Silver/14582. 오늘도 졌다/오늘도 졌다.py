# 울림 제미니스와 스타트링크 걸리버스의 각 이닝별 득점 입력 받기
gems = list(map(int, input().split()))
star = list(map(int, input().split()))

# 각 팀의 누적 점수 초기화
gems_sum = 0
star_sum = 0

# 각 이닝에서 누적 점수 계산 및 울림 제미니스가 이기고 있는지 확인
for i in range(9):
    gems_sum += gems[i]
    if gems_sum > star_sum:
        print("Yes")
        break
    star_sum += star[i]
else:
    print("No")
