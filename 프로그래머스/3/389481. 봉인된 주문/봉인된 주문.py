POW26 = [1]
PREFIX_POW = [0]
p = 1
for _ in range(11):
    p *= 26
    POW26.append(p)
    PREFIX_POW.append(PREFIX_POW[-1] + p)

def get_index(s):
    L = len(s)
    idx = PREFIX_POW[L-1]
    local_idx = 0
    for i in range(L):
        v = ord(s[i]) - ord('a')
        local_idx += v * POW26[L - 1 - i]
    return idx + local_idx + 1

def get_string(k):
    L = 0
    for i in range(1, 12):
        if k <= PREFIX_POW[i]:
            L = i
            break
    k -= PREFIX_POW[L-1]
    k -= 1
    s = ""
    for i in range(L - 1, -1, -1):
        p = POW26[i]
        v = k // p
        s += chr(ord('a') + v)
        k %= p
    return s

def solution(n, bans):
    bN = []
    for b_str in bans:
        bN.append(get_index(b_str))
    bN.sort()
    k = n
    for b_idx in bN:
        if b_idx <= k:
            k += 1
        else:
            break
    return get_string(k)