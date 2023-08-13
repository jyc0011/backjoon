n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = []
visited = set()

def permutation(pick):
    if pick == m:
        current_permutation = " ".join(map(str, result))
        if current_permutation in visited:
            return
        print(current_permutation)
        visited.add(current_permutation)
        return
    
    for i in range(len(numbers)):
        result.append(numbers[i])
        permutation(pick + 1)
        result.pop()

permutation(0)
