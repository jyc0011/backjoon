import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

used = [0] * 100001
left = 0
right = 0
ans = 0

while right < n:
    if used[li[right]] == 0:
        used[li[right]] = 1
        ans += (right - left + 1)
        right += 1
    else:
        used[li[left]] = 0
        left += 1

print(ans)