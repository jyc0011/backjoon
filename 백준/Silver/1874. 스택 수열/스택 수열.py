import sys

stack = []
result = []
count = 0
temp = True

for i in range(int(sys.stdin.readline())):
    num = int(int(sys.stdin.readline()))

    while count < num:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for i in result:
        print(i)
