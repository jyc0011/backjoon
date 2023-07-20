N = int(input())
binary_N = bin(N)[2:][::-1]
result = int(binary_N, 2)
print(result)
