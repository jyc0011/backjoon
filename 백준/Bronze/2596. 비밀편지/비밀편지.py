def HammingDistance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def solve():
    code = {'A': '000000', 'B': '001111', 'C': '010011', 'D': '011100',
            'E': '100110', 'F': '101001', 'G': '110101', 'H': '111010'}
    N = int(input())
    message = input()
    result = ''

    for i in range(N):
        segment = message[i*6:(i+1)*6]
        decode = ''

        for ch, binary in code.items():
            if HammingDistance(segment, binary) <= 1:
                if decode:
                    print(i + 1)
                    return
                decode = ch
        if not decode:
            print(i + 1)
            return

        result += decode

    print(result)

solve()
