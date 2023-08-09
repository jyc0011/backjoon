import math

def min_squares_sum(n):
    sqrt_n = int(math.sqrt(n))

    # √n이 정수일 때
    if sqrt_n * sqrt_n == n:
        return 1

    # √(n - i^2)이 정수일 때
    for i in range(1, sqrt_n + 1):
        n_minus_i2 = n - i**2
        sqrt_n_minus_i2 = int(math.sqrt(n_minus_i2))
        if sqrt_n_minus_i2 * sqrt_n_minus_i2 == n_minus_i2:
            return 2

    # √(n - i^2 - j^2)이 정수일 때
    for i in range(1, sqrt_n + 1):
        n_minus_i2 = n - i**2
        sqrt_n_minus_i2 = int(math.sqrt(n_minus_i2))
        for j in range(1, sqrt_n_minus_i2 + 1):
            n_minus_i2_j2 = n_minus_i2 - j**2
            sqrt_n_minus_i2_j2 = int(math.sqrt(n_minus_i2_j2))
            if sqrt_n_minus_i2_j2 * sqrt_n_minus_i2_j2 == n_minus_i2_j2:
                return 3

    # 남은 경우는 4
    return 4

n = int(input())
print(min_squares_sum(n))
