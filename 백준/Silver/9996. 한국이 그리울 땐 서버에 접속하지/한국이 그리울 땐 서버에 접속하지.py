n = int(input())
pattern = input().split('*')

for _ in range(n):
    file = input()
    if len(file) >= len(pattern[0] + pattern[1]) and pattern[0] == file[:len(pattern[0])] and pattern[1] == file[-len(pattern[1]):]:
        print("DA")
    else:
        print("NE")
