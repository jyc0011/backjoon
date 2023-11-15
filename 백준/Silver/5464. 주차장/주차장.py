import sys


def calculate_total_income(N, M, R, W, order):
    parking_spaces = [True] * N
    waiting_queue = []
    car_parking = [-1] * M
    total_income = 0

    for car in order:
        if car > 0:
            car -= 1
            available_space = -1
            for i in range(N):
                if parking_spaces[i]:
                    available_space = i
                    break
            if available_space >= 0:
                parking_spaces[available_space] = False
                car_parking[car] = available_space
            else:
                waiting_queue.append(car)
        else:
            car = -car - 1
            space = car_parking[car]
            total_income += W[car] * R[space]
            parking_spaces[space] = True
            if waiting_queue:
                waiting_car = waiting_queue.pop(0)
                parking_spaces[space] = False
                car_parking[waiting_car] = space

    return total_income


n, m = map(int, sys.stdin.readline().rstrip().split())
R = [int(sys.stdin.readline()) for _ in range(n)]
W = [int(sys.stdin.readline()) for _ in range(m)]
order = [int(sys.stdin.readline()) for _ in range(2*m)]

print(calculate_total_income(n, m, R, W, order))