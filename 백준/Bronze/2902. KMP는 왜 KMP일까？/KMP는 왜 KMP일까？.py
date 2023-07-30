name = input()
short_name = ""
for char in name:
    if char.isupper():
        short_name += char
print(short_name)