vowels = 'aeiou'

while True:
    word = input()
    if word == '#':
        break
    if word[0] in vowels:
        print(word + 'ay')
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                print(word[i:] + word[:i] + 'ay')
                break
        else:
            print(word + 'ay')
