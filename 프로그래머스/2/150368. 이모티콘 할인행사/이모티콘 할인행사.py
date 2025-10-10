from itertools import product

def solution(users, emoticons):
    sale = [10, 20, 30, 40]
    num = len(emoticons)
    answer = [0, 0]
    comb = product(sale, repeat=num)
    for c in comb:
        sub = 0
        saleNow = 0
        for ratio, price in users:
            purchase = 0
            for i in range(num):
                if c[i] >= ratio:
                    priceDis = emoticons[i] * (100 - c[i]) / 100
                    purchase += priceDis
            if purchase >= price:
                sub += 1
            else:
                saleNow += purchase
        if sub > answer[0]:
            answer = [sub, saleNow]
        elif sub == answer[0]:
            if saleNow > answer[1]:
                answer = [sub, saleNow]
    return answer