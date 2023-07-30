import sys

n, k = map(int, sys.stdin.readline().split())
countries = []

for _ in range(n):
    country, gold, silver, bronze = map(int, sys.stdin.readline().split())
    countries.append((gold, silver, bronze, country))

countries.sort(reverse=True)

for i in range(n):
    if countries[i][3] == k:
        print(i + 1)
        break