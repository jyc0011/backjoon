import sys
input = sys.stdin.readline

n = int(input().strip())
out = []

for _ in range(n):
    nums = list(map(int, input().split()))
    T, soldiers = nums[0], nums[1:]
    half = T // 2
    cand, cnt = None, 0
    for s in soldiers:
        if cnt == 0:
            cand, cnt = s, 1
        elif s == cand:
            cnt += 1
        else:
            cnt -= 1
    if cand is not None and soldiers.count(cand) > half:
        out.append(str(cand))
    else:
        out.append("SYJKGW")
sys.stdout.write("\n".join(out))