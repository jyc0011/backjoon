import sys

class Contestant:
    def __init__(self, id, score, submission, time):
        self.id = id
        self.score = score
        self.submission = submission
        self.time = time

contestants = []
for i in range(int(sys.stdin.readline())):
    s,c,l = map(int, sys.stdin.readline().split())
    contestants.append(Contestant(i+1, s, c, l))

contestants.sort(key=lambda x: (-x.score, x.submission, x.time))

print(contestants[0].id)