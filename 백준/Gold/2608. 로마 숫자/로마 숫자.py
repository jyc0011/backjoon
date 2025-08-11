import sys
input = sys.stdin.readline

mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
case = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def toI(s):
    ans = 0
    for i in range(len(s)):
        if i + 1 < len(s) and mapping[s[i]] < mapping[s[i+1]]:
            ans -= mapping[s[i]]
        else:
            ans += mapping[s[i]]
    return ans

def toR(num):
    ans = []
    for v, s in case:
        while num >= v:
            ans.append(s)
            num -= v
    return ''.join(ans)

input1 = input().strip()
input2 = input().strip()
ans = toI(input1) + toI(input2)

print(ans)
print(toR(ans))