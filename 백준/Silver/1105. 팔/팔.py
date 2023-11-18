A, B = map(str, input().split(' '))
cnt = 0
if len(A) != len(B):
    print(0)
else: 
    for i in range(len(A)):
        if A[i] == B[i]:
            if A[i] == '8':
                cnt += 1
        else:
            break
    print(cnt)