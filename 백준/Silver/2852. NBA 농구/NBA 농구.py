t1=0
t2=0
state=0
for i in range(int(input())):
    team, time=input().split()
    m,s=map(int, time.split(':'))
    if team=='1':
        if state==0:
            t1+=48*60-(60*m+s)
        state+=1
        if state==0:
            if t2>0:
                t2=t2-(48*60-(60*m+s))
    else: 
        if state==0:
            t2+=48*60-(60*m+s)
        state-=1
        if state==0:
            if t1>0:
                t1=t1-(48*60-(60*m+s))

print('{:0>2}:{:0>2}'.format(t1//60,t1%60))
print('{:0>2}:{:0>2}'.format(t2//60,t2%60))