import collections

def solution(points, routes):
    answer = 0
    paths = []
    max_ = 0
    for r in routes:
        temp = []
        pointS = r[0]
        s = points[pointS - 1]
        temp.append(s)
        
        for i in range(len(r) - 1):
            pointE = r[i+1]
            E = points[pointE - 1]
            nowR, nowE = temp[-1]
            pointER, pointEC = E
            dr = pointER - nowR
            dc = pointEC - nowE
            cntR = (dr > 0) - (dr < 0)
            for _ in range(abs(dr)):
                nowR += cntR
                temp.append([nowR, nowE])
                
            cntC = (dc > 0) - (dc < 0)
            for _ in range(abs(dc)):
                nowE += cntC
                temp.append([nowR, nowE])
                
        paths.append(temp)
        max_ = max(max_, len(temp))
        
    for t in range(max_):
        time = collections.Counter()
        for idR in range(len(paths)):
            path = paths[idR]
            if t < len(path):
                coord = path[t]
                coord_tuple = tuple(coord)
                time[coord_tuple] += 1
                
        for coord, count in time.items():
            if count >= 2:
                answer += 1
                
    return answer