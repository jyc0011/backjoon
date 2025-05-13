import sys, heapq
input = sys.stdin.readline
INF = 10**9

def vid(line, idx):
    return offset[line-1] + idx - 1

def dijkstra(T, s, t):
    dist = [INF]*V
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == t: 
            return d
        for v, is_tr in adj[u]:
            w = T if is_tr else 1
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist[t]

N = int(input())
line = list(map(int, input().split()))
offset = [0]
for sz in line:
    offset.append(offset[-1] + sz)
    
V = offset[-1]
adj = [[] for _ in range(V)]
for line, sz in enumerate(line, start=1):
    for i in range(1, sz):
        u, v = vid(line, i), vid(line, i+1)
        adj[u].append((v, 0))
        adj[v].append((u, 0))

M = int(input())
for _ in range(M):
    p1, p2, q1, q2 = map(int, input().split())
    u, v = vid(p1, p2), vid(q1, q2)
    adj[u].append((v, 1))
    adj[v].append((u, 1))

K = int(input())
for _ in range(K):
    T, u1, u2, v1, v2 = map(int, input().split())
    s = vid(u1, u2)
    t = vid(v1, v2)
    print(dijkstra(T, s, t))