import sys

input = sys.stdin.readline

N, K = map(int, input().split())
one_count = bin(N).count('1')

# 1의 개수가 K 이하 물병 추가X
if one_count <= K:
    print(0)
    exit()

# 그렇지 않은 경우, 상위 비트로 이동하며 필요한 물병의 수 계산
temp = N  # 원래의 N 값을 저장해둡니다.
while True:
    # N을 1씩 증가시키며 다음으로 set 되어있는 비트 위치를 찾기
    N += 1
    # 이진 표현에서 1의 개수를 계산
    one_count = bin(N).count('1')
    # 1의 개수가 K 이하면 반복을 종료
    if one_count <= K:
        break

# 필요한 물병의 수는 (증가시킨 N) - 원래의 N
print(N - temp)
