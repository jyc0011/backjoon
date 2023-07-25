import math

message = input()
n = len(message)
c = int(math.sqrt(n))

while n % c != 0:
    c -= 1

r = n // c
decoded_message = []

matrix = [message[i*c:i*c+c] for i in range(r)]
decoded_message = ''.join(''.join(matrix[j][i] for j in range(r)) for i in range(c))

print(''.join(decoded_message))
