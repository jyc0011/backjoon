def caesar_cipher(text, key):

    ciphertext = ""
    for i, c in enumerate(text):
        ciphertext += chr(65 + (ord(c) + ord(key[i % len(key)]) - 129) % 26)

    return ciphertext

while True:
    key = input()
    if key == "0":
        break
    text = input()
    ciphertext = caesar_cipher(text, key)
    print(ciphertext)