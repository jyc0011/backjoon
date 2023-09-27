n, k = map(int, input().split())
temp = list(map(int, input().split()))

result = sum(temp[:k])

for i in range(1, n-k+1):
    temp_ = temp[i:i+k]
    result = max(result, sum(temp_))

print(result)