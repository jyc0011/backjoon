arr = [list(input()) for _ in range(8)]
num=0
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0 and arr[i][j]=="F":
            num+=1
print(num)