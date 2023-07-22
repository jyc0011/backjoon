# 문자열 입력 받기
word = input()

# "CAMBRIDGE"에 속하는 모든 문자 제거
for char in "CAMBRIDGE":
    word = word.replace(char, "")

# 결과 출력
print(word)
