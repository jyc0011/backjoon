import sys
from collections import deque
from bisect import bisect_right

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
M_list = sorted(list(map(int, input().rstrip().split())))
K_list = deque(map(int, input().rstrip().split()))
visited = [False] * (len(M_list) + 1)

for _ in range(K):
    right_idx = bisect_right(M_list,K_list.popleft())
    while True:
        if not visited[right_idx]:
            visited[right_idx] = True
            print(M_list[right_idx])
            break
        else:
            right_idx += 1