import sys

input = sys.stdin.readline

def calc(mix_color, target):
    return abs(mix_color[0] - target[0]) + abs(mix_color[1] - target[1]) + abs(mix_color[2] - target[2])

def mix(idx, depth, r_, g_, b_, cnt):
    if depth >= 2:
        mix_color = (r_ // depth, g_ // depth, b_ // depth)
        diff_val = calc(mix_color, target)
        cnt = min(cnt, diff_val)
        if cnt == 0:
            return cnt
    if depth == 7 or idx >= n:
        return cnt
    r, g, b = paints[idx]
    cnt = mix(idx + 1, depth + 1, r_ + r, g_ + g, b_ + b, cnt)
    cnt = mix(idx + 1, depth, r_, g_, b_, cnt)
    return cnt

n = int(input())
paints = [tuple(map(int, input().split())) for _ in range(n)]
target = tuple(map(int, input().split()))
cnt = mix(0, 0, 0, 0, 0, float('inf'))
print(cnt)