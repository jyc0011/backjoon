def solution(s):
    answer = True
    queue=[]
    for i in range(len(s)):
        if s[i]==')':
            if not queue:
                return False
            else:
                queue.pop()
        else:
            queue.append('(')
    if queue:
        return False
    return True