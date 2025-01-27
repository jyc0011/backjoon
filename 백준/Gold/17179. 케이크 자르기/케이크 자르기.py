import sys

input = sys.stdin.readline

def can_cut(x, points, cnt):
    last = 0
    cnt_temp = 0
    for p in points:
        if p - last >= x:
            cnt_temp += 1
            last = p
    if L - last >= x:
        cnt_temp += 1
    return cnt_temp >= cnt + 1
    
def find(points, cnt):
    left, right = 1, L
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if can_cut(mid, points, cnt):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
    
N, M, L = map(int, input().split())
points = [int(input()) for _ in range(M)]
Q = [int(input()) for _ in range(N)]
for cnt in Q:
    print(find(points, cnt))