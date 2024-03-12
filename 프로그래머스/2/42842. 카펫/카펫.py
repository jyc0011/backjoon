def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            w = yellow // i + 2
            h = i + 2
            if brown == (w * h) - yellow:
                return [w, h]