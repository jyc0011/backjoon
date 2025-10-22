import sys

sys.setrecursionlimit(2000)
input = sys.stdin.readline

def solve():
    N = int(input())
    foods = []
    for _ in range(N):
        foods.append(list(map(int, input().split())))

    def find_max(time, mask):
        max_time = time

        for i in range(N):
            if not (mask & (1 << i)):
                p, s = foods[i]
                
                if p >= time:
                    res = find_max(time + s, mask | (1 << i))
                    max_time = max(max_time, res)

        return max_time

    return find_max(0, 0)


T = int(input())
for t in range(T):
    ans=solve()
    print(f'Case #{t + 1}: {ans}')