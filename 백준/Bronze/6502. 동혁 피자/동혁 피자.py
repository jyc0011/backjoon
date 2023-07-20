import math
import sys

test_case = 0
while True:
    li = list(map(int, sys.stdin.readline().split()))
    if li[0] == 0:
        break
    test_case += 1
    r, w, l = li[0], li[1], li[2]
    pizza_diameter = math.sqrt(w**2 + l**2)
    if pizza_diameter <= 2 * r:
        print("Pizza %d fits on the table." % test_case)
    else:
        print("Pizza %d does not fit on the table." % test_case)