def dfs(num, li):
    if num:
        li.append(int(num))
    if len(num) == 10:
        return
    last_digit = int(num[-1]) if num else 10
    for d in range(last_digit - 1, -1, -1):
        dfs(num + str(d),li)

def calc():
    li = []
    for start in range(10):
        dfs(str(start),li)
    return sorted(li)

def n_find(n):
    dec_nums = calc()
    if n < len(dec_nums):
        return dec_nums[n]
    else:
        return -1

n = int(input())
print(n_find(n))