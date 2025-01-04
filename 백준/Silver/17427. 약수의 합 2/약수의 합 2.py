def calc_g(n):
    f=[0]*(n+1)
    for i in range(1,N+1): # O(n)
        for j in range(i, N+1, i): # O(n/i) -> O(nlog(n))
            f[j]+=i
    g=0
    for i in range(1,N+1): # O(n)
        g+=f[i]
    return g    

N=int(input())
print(calc_g(N))