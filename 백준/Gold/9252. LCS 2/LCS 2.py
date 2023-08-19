import sys

def lcs(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs_str = ""
    i, j = len_s1, len_s2
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            lcs_str = s1[i - 1] + lcs_str
            i -= 1
            j -= 1

    return dp[len_s1][len_s2], lcs_str

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

length, result = lcs(s1, s2)
print(length)
if length:
    print(result)