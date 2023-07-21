N = int(input())
s = list(input().strip())

for i in range(N // 2):
    if s[i] == s[N-i-1] == '?':
        s[i] = s[N-i-1] = 'a'
    elif s[i] == '?':
        s[i] = s[N-i-1]
    elif s[N-i-1] == '?':
        s[N-i-1] = s[i]

if N % 2 and s[N // 2] == '?':
    s[N // 2] = 'a'

print(''.join(s) if s == s[::-1] else "Cannot be restored to a palindrome")