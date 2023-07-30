def life_score(s):
    score = sum(ord(c) - ord('A') + 1 for c in s if c != ' ')
    return "PERFECT LIFE" if score == 100 else score

N = int(input())
for _ in range(N):
    print(life_score(input()))