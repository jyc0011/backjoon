import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
live = [0] * (N + 1)
for i in range(N):
    person = A[i]
    house = i + 1
    live[person] = house
for _ in range(M):
    L, R = map(int, input().split())
    nowA = list(A) 
    people = list(range(L, R + 1))
    houses = []
    for p in people:
        houses.append(live[p])
    houses.sort()
    for i in range(len(people)):
        p = people[i]
        h = houses[i]
        nowA[h - 1] = p
    print(*nowA)