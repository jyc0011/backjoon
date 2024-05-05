from collections import deque

def calc(word1, word2):
    diff_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque([(begin, 0)])
    visited = set([begin]) 
    while queue:
        current_word, step_count = queue.popleft()

        if current_word == target:
            return step_count

        for word in words:
            if word not in visited and calc(current_word, word):
                visited.add(word)
                queue.append((word, step_count + 1))
                
    return 0