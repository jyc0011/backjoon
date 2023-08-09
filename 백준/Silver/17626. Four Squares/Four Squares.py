N = int(input())
dp = [0, 1]  # dp[i]: 숫자 i를 1보다 큰 제곱수들의 합으로 표현할 때 필요한 최소 제곱수의 개수

for i in range(2, N + 1):
    min_count = 1e9  # 최소 개수를 저장할 변수
    j = 1

    while j ** 2 <= i:
        min_count = min(min_count, dp[i - (j ** 2)])
        j += 1

    dp.append(min_count + 1)

print(dp[N])
