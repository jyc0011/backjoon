import sys
import heapq

input = sys.stdin.readline

n = int(input())
dasom_votes = int(input())
other_votes = []

for _ in range(n - 1):
    vote = int(input())
    heapq.heappush(other_votes, -vote)

bribes = 0
while other_votes:
    max_vote = -heapq.heappop(other_votes)
    if max_vote >= dasom_votes:
        max_vote -= 1
        dasom_votes += 1
        bribes += 1
        heapq.heappush(other_votes, -max_vote)
    else:
        break

print(bribes)