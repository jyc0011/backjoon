import sys
input = sys.stdin.readline

n=int(input())
for _ in range(n):
    li=list(map(int,input().split()))
    T, soldiers = li[0], li[1:]
    cand, cnt = None, 0
    for s in soldiers:
        if cnt == 0:
            cand, cnt = s, 1
        elif s == cand:
            cnt += 1
        else:
            cnt -= 1

    if cand is not None and soldiers.count(cand) > T // 2:
        print(cand)
    else:
        print("SYJKGW")