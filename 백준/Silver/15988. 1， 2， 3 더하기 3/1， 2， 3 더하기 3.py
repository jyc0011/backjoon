import sys

T = int(sys.stdin.readline().strip())
dp = dict()
dp[1] = 1
dp[2] = 2
dp[3] = 4
last_calculated = 3

for _ in range(T):
    number = int(sys.stdin.readline().strip())

    if number in dp:
        print(dp[number])

    else:
        for i in range(last_calculated + 1, number + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

        print(dp[number])

        last_calculated = number
