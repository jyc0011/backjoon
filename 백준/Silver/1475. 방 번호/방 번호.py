import math

n = input()
n_list = [0]*10

for i in n:
    n_list[int(i)] += 1

n_list[6] = math.ceil((n_list[6] + n_list[9]) / 2)
n_list[9] = 0

print(max(n_list))
