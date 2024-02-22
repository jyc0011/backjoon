import sys
from collections import deque
   
T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr_str = sys.stdin.readline().rstrip()[1:-1]
    if arr_str == "":
        li = deque()
    else:
        li = deque(map(int, arr_str.split(',')))
        
    reverse_flag = False
    error_flag = False

    for op in p:
        if op == 'R':
            reverse_flag = not reverse_flag
        elif op == 'D':
            if not li:
                error_flag = True
                break
            if reverse_flag:
                li.pop()
            else:
                li.popleft()

    if error_flag:
        print("error")
    else:
        if reverse_flag:
            li.reverse()
        print("[" + ",".join(map(str, li)) + "]")