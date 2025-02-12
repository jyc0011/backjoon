from collections import defaultdict

def solution(tickets):
    g = defaultdict(list)
    for s, e in tickets:
        g[s].append(e)
    for s in g:
        g[s].sort(reverse=True)

    stk = ["ICN"]
    res = []
    while stk:
        while g[stk[-1]]:
            stk.append(g[stk[-1]].pop())
        res.append(stk.pop())
    return res[::-1]