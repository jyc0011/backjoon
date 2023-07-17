N, M = map(int, input().split())
passwords = {}

for _ in range(N):
    site, pw = input().split()
    passwords[site] = pw

for _ in range(M):
    print(passwords[input()])
