import sys
input = sys.stdin.readline

def taxi_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def get_w_catch(k, t, mosquitoes):
    d = [[0]*k for _ in range(k)]
    for i in range(k):
        r1, c1, _ = mosquitoes[i]
        for j in range(k):
            if i != j:
                r2, c2, _ = mosquitoes[j]
                d[i][j] = taxi_dist(r1, c1, r2, c2)
    INF = 10**15
    dp = [[INF]*k for _ in range(1 << k)]
    for i in range(k):
        dp[1 << i][i] = 0
    for msk in range(1 << k):
        for lst in range(k):
            if dp[msk][lst] == INF:
                continue
            cur_cost = dp[msk][lst]
            for nxt in range(k):
                if msk & (1 << nxt):
                    continue
                nxt_mask = msk | (1 << nxt)
                nxt_cost = cur_cost + d[lst][nxt]
                if nxt_cost < dp[nxt_mask][nxt]:
                    dp[nxt_mask][nxt] = nxt_cost
    w_catch = 0
    for msk in range(1 << k):
        cnt = bin(msk).count('1')
        feasible = False
        for lst in range(k):
            if dp[msk][lst] <= t:
                feasible = True
                break
        if feasible and cnt > w_catch:
            w_catch = cnt
    return w_catch

def get_a_catch(n, m, p, mosquitoes):
    a_catch = 0
    for r in range(1, n+1):
        for c in range(1, m+1):
            count_kill = 0
            for (mr, mc, s) in mosquitoes:
                dist_rc = abs(r - mr) + abs(c - mc)
                if dist_rc == 0:
                    count_kill += 1
                else:
                    if p >= dist_rc * s:
                        count_kill += 1
            a_catch = max(a_catch, count_kill)
    return a_catch


n, m, k, t, p = map(int, input().split())
mosquitoes = [tuple(map(int, input().split())) for _ in range(k)]
    
w_result = get_w_catch(k, t, mosquitoes)
a_result = get_a_catch(n, m, p, mosquitoes)
print(w_result, a_result)