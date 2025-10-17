N=int(input())
li=list(map(int,input().split()))
prefix=[False for _ in range(N)]
suffix=[False for _ in range(N)]
prefix[0],suffix[N-1]=True,True
for i in range(1,N):
	if li[i-1]<=li[i]:
		prefix[i]=prefix[i-1]
	else:
		break
for i in range(N-2, -1, -1):
	if li[i]<=li[i+1]:
		suffix[i]=suffix[i+1]
	else:
		break
cnt=0
for i in range(N):
	if i == 0 :
		if suffix[1]:
			cnt+=1
	elif i == N-1:
		if prefix[N-2]:
			cnt+=1
	else:
		if prefix[i-1] and suffix[i+1] and li[i-1]<=li[i+1]:
			cnt+=1
print(cnt)