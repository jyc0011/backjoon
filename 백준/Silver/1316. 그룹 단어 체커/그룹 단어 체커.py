n = int(input())
group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성
        if word[index] != word[index+1]:  # 연속되는 문자가 다를 때
            new_word = word[index+1:]  # 현재 글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 새로운 단어에서 현재 문자가 존재한다면
                error += 1  # 에러 카운트
    if error == 0:  
        group_word += 1  # 그룹 단어 카운트 증가
print(group_word)
