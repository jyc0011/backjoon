import sys
input = sys.stdin.readline

def calc(houses, n, c, min_dist):
    cnt = 1
    last_placed = houses[0]
    for i in range(1, n):
        if houses[i] - last_placed >= min_dist:
            cnt += 1
            last_placed = houses[i]
            if cnt == c:
                return True
    return False

def find(n, c, houses):
    houses.sort()
    l = 1
    h = houses[-1] - houses[0]
    ans = 0
    while l <= h:
        m = (l + h) // 2
        if calc(houses, n, c, m):
            ans = m
            l = m + 1
        else:
            h = m - 1
    return ans

n, c = map(int, input().strip().split())
houses = [int(input().strip()) for _ in range(n)]

print(find(n, c, houses))