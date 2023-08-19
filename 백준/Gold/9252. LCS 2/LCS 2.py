A = input()
B = input()

dp = [[0] * 1001 for _ in range(1001)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lcs_str = ""
i, j = len(A), len(B)
while i > 0 and j > 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        lcs_str = A[i-1] + lcs_str
        i -= 1
        j -= 1

print(dp[len(A)][len(B)])

if dp[len(A)][len(B)]:
    print(lcs_str)