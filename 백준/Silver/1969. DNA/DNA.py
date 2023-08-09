import sys

n, m = map(int, sys.stdin.readline().split())

seq = []
s = ''
dna = ['A', 'C', 'G', 'T']
hamming_dist = 0

for _ in range(n):
    data = sys.stdin.readline().strip()
    seq.append(data)

for i in range(m):
    counts = [0] * 4
    for j in range(n):
        counts[dna.index(seq[j][i])] += 1
    selected_dna = dna[counts.index(max(counts))]
    s += selected_dna
    for k in range(n):
        if seq[k][i] != selected_dna:
            hamming_dist += 1

print(s)
print(hamming_dist)
