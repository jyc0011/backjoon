def calc_g(n):
    g=0
    for i in range(1,N+1): # O(n)
        g+=i*(N//i)
    return g

N=int(input())
print(calc_g(N))