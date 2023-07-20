def find_chefs():
    L = int(input())
    N = int(input())
    cake = [0] * 1001
    expected_chef = -1
    actual_chef = -1
    max_expected = -1
    max_actual = -1
    actual_pieces = [0] * (N+1)

    for i in range(1, N+1):
        P, K = map(int, input().split())
        if max_expected < K-P+1:
            max_expected = K-P+1
            expected_chef = i
        for j in range(P, K+1):
            if cake[j] == 0:
                cake[j] = i
                actual_pieces[i] += 1
        if max_actual < actual_pieces[i]:
            max_actual = actual_pieces[i]
            actual_chef = i

    print(expected_chef)
    print(actual_chef)

find_chefs()
