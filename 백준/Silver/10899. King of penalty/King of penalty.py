import sys
input = sys.stdin.readline

P, N = map(int, input().split())
times = sorted(list(map(int, input().split())))
cnt,time = 0,0
for t in times:
    if time + t >= P:
        break
    time += t
    cnt += 1

chosen = times[:cnt][::-1]

ans = 0
current_time = (P - 1) - time

for t in chosen:
    current_time += t
    ans += current_time

print(cnt, ans)