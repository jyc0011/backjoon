N, K = map(int, input().split())
max_val = max(int(str(i*N)[::-1]) for i in range(1, K+1))
print(max_val)
