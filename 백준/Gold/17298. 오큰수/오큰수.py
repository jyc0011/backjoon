import sys

input=sys.stdin.readline

def NGE(n,arr):
    result = [-1] * n
    stack = []
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)
    return result

N= int(input())
A=list(map(int,input().rstrip().split()))
print(*NGE(N,A))