n, k = map(int, input().split())

def pascal(n, k):
    if k == 0 or k == n:
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)

result = pascal(n - 1, k - 1)
print(result)