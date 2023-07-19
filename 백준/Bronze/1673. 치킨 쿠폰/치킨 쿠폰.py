import sys

while True:
    try:
        n, k = map(int,sys.stdin.readline().split())
        cnt= 0
        cnt += n
        while n//k:
            cnt += n//k
            n=n//k+n%k
        print(cnt)

    except:
        break
