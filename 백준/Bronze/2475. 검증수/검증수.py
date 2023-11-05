numbers = list(map(int, input().split()))
sum_of_squares = sum(x**2 for x in numbers)
verification_number = sum_of_squares % 10
print(verification_number)
