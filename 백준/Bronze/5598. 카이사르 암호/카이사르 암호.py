def caesar_cipher(s):
    result = ""
    for char in s:
        result += chr((ord(char) - 68) % 26 + 65)
    return result

print(caesar_cipher(input()))