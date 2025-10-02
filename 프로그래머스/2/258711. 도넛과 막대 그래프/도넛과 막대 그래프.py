from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    out = defaultdict(int)
    in_ = defaultdict(int)
    n = set()
    for u, v in edges:
        out[u] += 1
        in_[v] += 1
        n.add(u)
        n.add(v)
    nodes = 0
    for node in n:
        if out[node] >= 2 and in_[node] == 0:
            nodes = node
            break
            
    answer[0] = nodes
    total = out[nodes]
    b = 0
    e = 0
    
    for node in n:
        if node == nodes:
            continue
        if out[node] == 0:
            b += 1
        if out[node] == 2 and in_[node] >= 2:
            e += 1
    answer[2] = b
    answer[3] = e
    answer[1] = total - b - e 
    return answer