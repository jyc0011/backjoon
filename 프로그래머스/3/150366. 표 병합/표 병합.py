def find(root, r, c):
    if root[r][c] == (r, c):
        return r, c
    x, y = root[r][c]
    root[r][c] = find(root, x, y)
    return root[r][c]

def solution(commands):
    root = [[(r, c) for c in range(51)] for r in range(51)]
    g = [[None for _ in range(51)] for _ in range(51)]
    answer = []

    for line in commands:
        c = line.split()
        op = c[0]
        if op == "UPDATE":
            if len(c) == 4:
                r, c_val, value = int(c[1]), int(c[2]), c[3]
                rootR, rootC = find(root, r, c_val)
                g[rootR][rootC] = value
            else:
                value1, value2 = c[1], c[2]
                for i in range(1, 51):
                    for j in range(1, 51):
                        rootR, rootC = find(root, i, j)
                        if g[rootR][rootC] == value1:
                            g[rootR][rootC] = value2
        elif op == "MERGE":
            r1, c1, r2, c2 = map(int, c[1:])
            if (r1, c1) != (r2, c2):
                rx1, ry1 = find(root, r1, c1)
                rx2, ry2 = find(root, r2, c2)
                if (rx1, ry1) != (rx2, ry2):
                    val1 = g[rx1][ry1]
                    val2 = g[rx2][ry2]
                    root[rx2][ry2] = (rx1, ry1)
                    if val1 is None and val2 is not None:
                        g[rx1][ry1] = val2
        elif op == "UNMERGE":
            r, c_val = map(int, c[1:])
            rootR, rootC = find(root, r, c_val)
            rootV = g[rootR][rootC]
            cells_to_unmerge = []
            for i in range(1, 51):
                for j in range(1, 51):
                    if find(root, i, j) == (rootR, rootC):
                        cells_to_unmerge.append((i, j))
            for i, j in cells_to_unmerge:
                root[i][j] = (i, j)
                g[i][j] = None
            if rootV is not None:
                g[r][c_val] = rootV
        elif op == "PRINT":
            r, c_val = map(int, c[1:])
            rootR, rootC = find(root, r, c_val)
            rootV = g[rootR][rootC]
            answer.append(rootV if rootV is not None else "EMPTY")
    return answer