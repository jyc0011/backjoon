def solution(friends, gifts):
    ans=0
    num = len(friends)
    idxF = {name: i for i, name in enumerate(friends)}
    mapG = [[0] * num for _ in range(num)]
    scoreG = [0] * num
    for gift in gifts:
        A, B = gift.split()
        numA = idxF[A]
        numB = idxF[B]
        mapG[numA][numB] += 1
        scoreG[numA] += 1
        scoreG[numB] -= 1
    next = [0] * num
    for i in range(num):
        for j in range(i + 1, num):
            i_gave = mapG[i][j]
            j_gave = mapG[j][i]
            if i_gave > j_gave:
                next[i] += 1
            elif j_gave > i_gave:
                next[j] += 1
            else:
                if scoreG[i] > scoreG[j]:
                    next[i] += 1
                elif scoreG[j] > scoreG[i]:
                    next[j] += 1
    ans=max(next)
    return ans