import sys
input = sys.stdin.readline

def calc(card, k, n):
    card = card[:]
    top = 2 ** k
    card = card[-top:] + card[:-top]
    for i in range(2, k + 2):
        move = 2 ** (k - i + 1)
        top_block = card[:top]
        rest = card[top:]
        card = top_block[-move:] + top_block[:-move] + rest
        top = move

    return card

N = int(input())
card = list(range(1, N + 1))
last = list(map(int, input().split()))
for K1 in range(1, 10):
    first = calc(card, K1, N)
    for K2 in range(1, 10):
        second = calc(first, K2, N)
        if second == last:
            print(K1, K2)
            sys.exit()