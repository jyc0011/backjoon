import sys
input = sys.stdin.readline

n, m = map(int, input().split())
need = []
cnt = 0
total = 0

for _ in range(n):
    P, L = map(int, input().split())
    bids = list(map(int, input().split()))
    if P < L:
        need.append(1)
    else:
        bids.sort(reverse=True)
        need.append(bids[L-1])

need.sort()
for x in need:
    if total + x > m:
        break
    total += x
    cnt += 1
print(cnt)