from collections import defaultdict, deque

def solution(nodes, edges):
    adj = defaultdict(list)
    line = defaultdict(int)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        line[u] += 1
        line[v] += 1
    visited = set()
    t, rt = 0, 0
    for i in nodes:
        if i not in visited:
            tree = []
            q = deque([i])
            visited.add(i)
            while q:
                node = q.popleft()
                tree.append(node)
                for n in adj[node]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
            oeR, oeC = 0, 0
            for node in tree:
                deg = line[node]
                if node % 2 == deg % 2:
                    oeR += 1
                if node % 2 == (deg - 1) % 2:
                    oeC += 1
            if oeR == 1 and oeC == len(tree) - 1:
                t += 1
            roeR, roeC = 0, 0
            for node in tree:
                deg = line[node]
                if node % 2 != deg % 2:
                    roeR += 1
                if node % 2 != (deg - 1) % 2:
                    roeC += 1
            if roeR == 1 and roeC == len(tree) - 1:
                rt += 1
    return [t, rt]