k = int(input())

# 초콜릿의 크기 결정
choco = 1
while k > choco:
    choco *= 2
print(choco, end=" ")
# 최소 분할 횟수 결정
n = 0
while True:
    if k % choco == 0:
        print(n)
        break
    else:
        choco //= 2
        n += 1