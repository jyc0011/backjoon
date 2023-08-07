import sys

N, M = map(int, sys.stdin.readline().split())
not_heard = set(sys.stdin.readline().rstrip() for _ in range(N))
not_seen = set(sys.stdin.readline().rstrip() for _ in range(M))

not_heard_seen = sorted(list(not_heard.intersection(not_seen)))

print(len(not_heard_seen))
for name in not_heard_seen:
    print(name)
