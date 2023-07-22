N = int(input())
count = 0

for _ in range(N):
    word = input()
    stack = []

    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        count += 1

print(count)
