n = int(input())
s = [0] * n
w = [0] * n
res = 0

for i in range(n):
    s[i], w[i] = map(int, input().split())

def solve(idx, eggs, broken_count):
    global res
    if idx == n:
        res = max(res, broken_count)
        return
    # 현재 계란이 이미 깨진 경우
    if eggs[idx] <= 0:
        solve(idx + 1, eggs, broken_count)
    else:
        flag = False
        for i in range(n):
            if i != idx and eggs[i] > 0:
                flag = True
                # 내구도 감소
                eggs[idx] -= w[i]
                eggs[i] -= w[idx]
                # 깨진 계란 수 갱신
                next_broken_count = broken_count + (eggs[idx] <= 0) + (eggs[i] <= 0)
                solve(idx + 1, eggs, next_broken_count)
                # 내구도 복원
                eggs[idx] += w[i]
                eggs[i] += w[idx]
        
        if not flag:
            solve(idx + 1, eggs, broken_count)

solve(0, s, 0)
print(res)