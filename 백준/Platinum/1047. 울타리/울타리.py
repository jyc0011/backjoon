import sys

input = sys.stdin.readline

n = int(input())
trees = []
for _ in range(n):
    trees.append(list(map(int, input().split())))
xCoords = [0] + [t[0] for t in trees]
yCoords = [0] + [t[1] for t in trees]
minK = n
for minX in xCoords:
    for maxX in xCoords:
        if minX > maxX: 
            continue
        for minY in yCoords:
            for maxY in yCoords:
                if minY > maxY: 
                    continue
                width = maxX - minX
                height = maxY - minY
                reqPerimeter = 2 * (width + height)
                cutTrees = []
                keptTrees = []
                for tree in trees:
                    x, y, length = tree
                    isInside = (minX <= x <= maxX) and (minY <= y <= maxY)
                    if isInside:
                        keptTrees.append(tree)
                    else:
                        cutTrees.append(tree)    
                currentLen = sum(t[2] for t in cutTrees)
                currentK = len(cutTrees)
                neededLen = reqPerimeter - currentLen
                if neededLen > 0:
                    keptTrees.sort(key=lambda t: t[2], reverse=True)
                    for tree in keptTrees:
                        currentLen += tree[2]
                        currentK += 1
                        neededLen -= tree[2]
                        if neededLen <= 0:
                            break
                if neededLen <= 0:
                    minK = min(minK, currentK)
print(minK)