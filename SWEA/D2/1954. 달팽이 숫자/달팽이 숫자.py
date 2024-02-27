dx=[0,1,0,-1]   # ->부터 시계 방향
dy=[1,0,-1,0]

for i in range(int(input())):
    n= int(input())
    snail=[[0]*n for _ in range(n)]
    x,y,d=0,0,0
    
    for z in range(1,n*n+1):
        snail[x][y]=z
        nx,ny=x+dx[d],y+dy[d]
        if nx<0 or nx>=n or ny<0 or ny>=n or snail[nx][ny]!=0: # 충돌시 방향 전환
            d=(d+1)%4
            nx,ny=x+dx[d],y+dy[d]
        x,y=nx,ny
        
    print(f'#{i+1}')  
    for r in snail:
        print(' '.join(map(str,r)))