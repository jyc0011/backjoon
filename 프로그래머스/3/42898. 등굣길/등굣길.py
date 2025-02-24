def solution(m, n, puddles):
    answer = 0
    MOD = 1000000007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    puddle_set = {(x, y) for x, y in puddles}
    dp[1][1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (x, y) in puddle_set:
                dp[y][x] = 0
            elif not (x == 1 and y == 1):
                dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD

    answer= dp[n][m] % MOD
    return answer