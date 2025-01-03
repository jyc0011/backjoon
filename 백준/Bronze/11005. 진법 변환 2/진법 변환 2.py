def convert(n, b):
    T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = []
    
    while n > 0:
        n, r = divmod(n, b)
        ans.append(T[r])
    return ''.join(reversed(ans))

N, B = map(int, input().split())
print(convert(N, B))