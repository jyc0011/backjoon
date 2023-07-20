def convert(n, b):
    T = "0123456789ABCDEF"
    q, r = divmod(n, b)
    if q == 0:
        return T[r]
    else:
        return convert(q, b) + T[r]

N, B = map(int, input().split())
print(convert(N, B))