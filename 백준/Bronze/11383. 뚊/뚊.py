import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

first_image = [sys.stdin.readline().rstrip() for _ in range(N)]
second_image = [sys.stdin.readline().rstrip() for _ in range(N)]

is_eyfa = True

for i in range(N):
    # 첫 번째 이미지의 각 문자를 두 번씩 반복한 문자열을 만든다.
    stretched_row = ''.join([char*2 for char in first_image[i]])
    # 해당 문자열과 두 번째 이미지의 행을 비교한다.
    if stretched_row != second_image[i]:
        is_eyfa = False
        break

if is_eyfa:
    print("Eyfa")
else:
    print("Not Eyfa")
