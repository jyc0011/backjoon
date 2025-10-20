def calc(N, d, t, l):
    r=t[0]
    for i in range(1,N):
        if d[i] >l:
            r+=((d[i]-l)*(t[i-1]+t[i])+t[i])
        else:
            r+=t[i]
    return r

def solution(diffs, times, limit):
    answer = max(diffs)
    l = 1
    h = max(diffs)
    N = len(diffs)
    while l <= h:
        m = (l+h)//2
        total = calc(N, diffs, times, m)
        if total > limit:
            l = m+1
        else:
            answer = min(answer, m)
            h = m-1  
    return answer