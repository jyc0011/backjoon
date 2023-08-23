import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()
num_li =[]

for i in range(n):
    num_li.append(int(sys.stdin.readline()))

stack = []

for i in word :					
    if 'A' <= i <= 'Z' :
        stack.append(num_li[ord(i)-ord('A')])
    else :
        str2 = stack.pop()
        str1 = stack.pop()

        if i =='+' :
            stack.append(str1+str2)
        elif i == '-' :
            stack.append(str1-str2)
        elif i == '*' :
            stack.append(str1*str2)
        elif i == '/' :
            stack.append(str1/str2)

print('%.2f' %stack[0])	