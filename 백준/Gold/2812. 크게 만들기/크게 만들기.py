N, K = map(int, input().split())
nums = list(map(int, str(input().strip())))

stack = []
cnt = K

for i in range(N):
    while cnt > 0 and stack:
        if stack[-1] < nums[i]:
            stack.pop()
            cnt -= 1
        else:
            break
    stack.append(nums[i])

while cnt > 0:
    stack.pop()
    cnt -= 1

print(''.join(map(str, stack)))
