T = int(input())

for test_case in range(1, T + 1):
    k = int(input())
    if k % 2 == 0:
        print("#" + str(test_case) + " Alice")
    else:
        print("#" + str(test_case) + " Bob")
