import sys

text = sys.stdin.read().replace('\n', '')  # 입력 받기

alphabet_count = [0]*26  # 각 알파벳 별 카운트를 저장할 리스트 초기화
max_count = 0  # 가장 많이 나온 글자의 등장 횟수를 저장할 변수 초기화

for c in text:
    if 'a' <= c <= 'z':  # c가 알파벳 소문자라면
        alphabet_count[ord(c) - ord('a')] += 1  # 해당 알파벳의 등장 횟수를 증가시킴
        max_count = max(max_count, alphabet_count[ord(c) - ord('a')])  # 가장 많이 나온 글자의 등장 횟수 업데이트

for i in range(26):
    if alphabet_count[i] == max_count:  # 만약 i번째 알파벳의 등장 횟수가 max_count와 같다면
        print(chr(i + ord('a')), end='')  # 해당 알파벳 출력
