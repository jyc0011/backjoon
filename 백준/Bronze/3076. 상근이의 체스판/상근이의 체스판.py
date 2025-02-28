# 완전탐색
# 문자열로 최적화

import sys
input = sys.stdin.readline
write = sys.stdout.write

R, C = map(int, input().split())
A, B = map(int, input().split())

row1 = "".join("X" * B if i % 2 == 0 else "." * B for i in range(C))
row2 = "".join("." * B if i % 2 == 0 else "X" * B for i in range(C))

for i in range(R):
    row_pattern = row1 if i % 2 == 0 else row2
    for _ in range(A):  
        write(row_pattern + "\n")