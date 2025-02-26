import sys
input = sys.stdin.readline
w, n = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
sums = set()
for i in range(n):
    for j in range(i+1, n):
        need = w - (A[i] + A[j])
        if need in sums:
            print("YES")
            sys.exit(0)
    for k in range(i):
        sums.add(A[k] + A[i])
        
print("NO")