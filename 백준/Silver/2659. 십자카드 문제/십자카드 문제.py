def clock(a, b, c, d):
    nums = [a, b, c, d]
    min_c = 9999
    for i in range(4):
        n = nums[i]*1000 + nums[(i+1)%4]*100 + nums[(i+2)%4]*10 + nums[(i+3)%4]
        min_c = min(min_c, n)
    return min_c

clocks = set()
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                clocks.add(clock(a, b, c, d))

sorted_clocks = sorted(clocks)

card = list(map(int, input().split()))
card_clock = clock(*card)

rank = sorted_clocks.index(card_clock) + 1
print(rank)