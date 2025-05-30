S = input().strip()

if 'A' in S:
    result = ''.join('A' if c in 'BCDF' else c for c in S)
elif 'B' in S:
    result = ''.join('B' if c in 'CDF' else c for c in S)
elif 'C' in S:
    result = ''.join('C' if c in 'DF' else c for c in S)
else:
    result = 'A' * len(S)

print(result)