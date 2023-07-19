s = input().upper()
counter = [0]*26

for char in s:
    counter[ord(char) - ord('A')] += 1

max_count = max(counter)
indices = [i for i, v in enumerate(counter) if v == max_count]  # 가장 많이 등장하는 알파벳의 인덱스를 찾음

if len(indices) > 1:
    print("?")
else:
    print(chr(indices[0] + ord('A')))