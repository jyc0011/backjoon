import sys

input=sys.stdin.readline

def max_people_eating_burger(N, K, s):
    count = 0
    s = list(s)

    for i in range(N):
        if s[i] == 'P':
            for j in range(i - K, i + K + 1):
                if 0 <= j < N and s[j] == 'H':
                    s[j] = 'X'
                    count += 1
                    break
    return count

N, K = map(int, input().split())
s = input().strip()
print(max_people_eating_burger(N, K, s))
