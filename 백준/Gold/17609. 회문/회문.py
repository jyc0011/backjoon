import sys

for _ in range(int(input())):
    text=sys.stdin.readline().rstrip()
    l, r = 0, len(text) - 1
    ans=0
    for _ in range(len(text)):
        if l >= r:
            break
        if text[l] == text[r]:
            l += 1
            r -= 1
            continue
        if text[l] == text[r-1]:
            check = text[l:r]
            if check[:] == check[::-1]:
                ans = 1
                break
        if text[l+1] == text[r]:
            check = text[l+1:r+1]
            if check[:] == check[::-1]:
                ans = 1
                break
        ans = 2
        break

    print(ans)