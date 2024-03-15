from itertools import permutations, chain, islice
import math
import sys

def make_no_repeats(length):
    my_iter = permutations(range(10), length)
    no_zero_start_index = math.perm(9, length - 1)
    no_lead_zeros = islice(my_iter, no_zero_start_index, None)

    return no_lead_zeros

while True:
    count = int(sys.stdin.readline())
    if count == 0:
        break
    iter_no_repeats = chain(*map(make_no_repeats, range(1, 11)))
    result_number = next(islice(iter_no_repeats, count - 1, None))
    print(''.join(map(str, result_number)))