def solution(sizes):
    x,y=0,0
    for i in sizes:
        w,h=i[0],i[1]
        if h>w:
            w,h=h,w
        if x < w:
            x=w
        if y < h :
            y=h
    answer=x*y
    return answer