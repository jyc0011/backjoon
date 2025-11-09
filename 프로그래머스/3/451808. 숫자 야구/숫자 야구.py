from itertools import permutations
from collections import defaultdict

def check(secret, guess):
    s = 0
    b = 0
    for i in range(4):
        if guess[i] == secret[i]:
            s += 1
    for i in range(4):
        if guess[i] != secret[i]:
            if guess[i] in secret:
                b += 1
    return f"{s}S {b}B"

def solution(n, submit):
    all_perms = [''.join(p) for p in permutations("123456789", 4)]
    cands = all_perms[:]
    first_guess = True
    while n > 0:
        if not cands:
            return -1
        if len(cands) == 1:
            guess = cands[0]
        elif first_guess:
            guess = '1234'
            first_guess = False
        else:
            min_max = float('inf')
            best_g = cands[0] 
            for g in all_perms: 
                counts = defaultdict(int)
                for c in cands: 
                    res = check(secret=c, guess=g)
                    counts[res] += 1
                max_cnt = max(counts.values())
                if max_cnt < min_max:
                    min_max = max_cnt
                    best_g = g
                elif max_cnt == min_max and g in cands and best_g not in cands:
                    best_g = g
            guess = best_g
        res = submit(int(guess))
        if res == "4S 0B":
            return int(guess)
        n -= 1
        next_cands = []
        for sec in cands:
            if check(sec, guess) == res:
                next_cands.append(sec)
        cands = next_cands
    return -1