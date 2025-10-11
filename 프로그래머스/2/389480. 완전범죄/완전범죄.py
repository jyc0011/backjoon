def solution(info, n, m):
    dp = [0] * m
    total = 0
    for a, b in info:
        total += a
        for j in range(m - 1, b - 1, -1):
            dp[j] = max(dp[j], dp[j - b] + a)
    save_ = max(dp)
    answer = total - save_
    if answer >= n:
        return -1
    else:
        return answer