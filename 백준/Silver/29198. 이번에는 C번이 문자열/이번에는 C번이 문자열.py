import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
S = [input().strip() for _ in range(N)]
S.sort()
selected = ''.join(S[:K])
result = ''.join(sorted(selected))
print(result)