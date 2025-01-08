A, B, C = input().split()
A, B = int(A), int(B)
C = int(C[-1]) % 2

if C == 0:
    print(A)
else:
    print(A ^ B)