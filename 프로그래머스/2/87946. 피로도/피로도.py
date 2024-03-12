def solution(k, dungeons):
    return dfs(k, dungeons, 0)


def dfs(x, dungeons, cnt):
    max_cnt = cnt
    for i, (min_x, y) in enumerate(dungeons):
        if x >= min_x:
            next_dungeons = dungeons[:i] + dungeons[i+1:]
            max_cnt = max(max_cnt, dfs(x - y, next_dungeons, cnt + 1))
    return max_cnt
