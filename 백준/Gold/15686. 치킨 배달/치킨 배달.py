import sys
from itertools import combinations

def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_city_chicken_distance(chicken_stores):
    distance = 0
    for h in house:
        distance += min([get_distance(h, c) for c in chicken_stores])
    return distance

n,m=map(int, sys.stdin.readline().rstrip().split())
city=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
house=[]
chicken=[]

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

answer = float('inf')

for stores in combinations(chicken, m):
    answer = min(answer, get_city_chicken_distance(stores))

print(answer)