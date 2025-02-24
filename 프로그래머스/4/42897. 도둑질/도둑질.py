import sys
sys.setrecursionlimit(10**7)

def dfs(i, memo, money):
    if i < 0:
        return 0
    if memo[i] != -1:
        return memo[i]
    pick = money[i] + dfs(i - 2, memo, money)
    skip = dfs(i - 1, memo, money)
    memo[i] = max(pick, skip)
    return memo[i]

def solution(money):
    n = len(money)
    if n < 3:
        return max(money)
    money1 = money[:-1]
    memo1 = [-1] * (n - 1)
    case1 = dfs(n - 2, memo1, money1)
    money2 = money[1:]
    memo2 = [-1] * (n - 1)
    case2 = dfs(n - 2, memo2, money2)
    return max(case1, case2)