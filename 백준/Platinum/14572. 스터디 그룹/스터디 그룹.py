import sys

n, k, d = map(int, sys.stdin.readline().split())
s = []
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))
    s[-1].append(list(map(int, sys.stdin.readline().split())))

# 실력을 기준으로 정렬
s.sort(key=lambda x: x[1])

l = 0
r = 0
algo = [0 for _ in range(k+1)]
ans = 0

# 처음 그룹의 알고리즘 정보 초기화
for i in s[0][2]:
    algo[i] += 1

while l < n:
    while r + 1 < n and s[r + 1][1] - s[l][1] <= d:
        r += 1
        for i in s[r][2]:
            algo[i] += 1

    all = 0
    person = 0

    # 그룹 내에서 알고리즘 개수와 개별 학생이 아는 알고리즘 수 계산
    for i in range(1, k+1):
        if algo[i] != 0:
            if algo[i] == r - l + 1:
                person += 1
            all += 1

    # 효율성 계산 및 최대값 갱신
    ans = max(ans, (all - person) * (r - l + 1))

    # 왼쪽 포인터 이동과 그에 따른 알고리즘 정보 업데이트
    for i in s[l][2]:
        algo[i] -= 1
    l += 1

# 최대 효율성 출력
print(ans)