from collections import defaultdict

def rolling_hash(strings, base=256, mod=10**9+7):
    hashes = []
    for s in strings:
        hash_val = 0
        for char in s:
            hash_val = (hash_val * base + ord(char)) % mod
        hashes.append(hash_val)
    return hashes

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

result = 0
start, end = 0, R-1
while start <= end:
    mid = (start+end)//2

    column_strings = [''.join(arr[i][j] for i in range(mid, R)) for j in range(C)]
    hashes = rolling_hash(column_strings)

    if len(hashes) == len(set(hashes)):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)