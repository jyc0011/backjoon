def solution(numbers):
    answer = []
    for n in numbers:
        bNum = bin(n)[2:]
        n = len(bNum)
        treeH = 0
        totalN = 0
        while totalN < n:
            treeH += 1
            totalN = 2**treeH - 1
        bNum = f'{bNum:>0{totalN}}'
        if calc(bNum):
            answer.append(1)
        else:
            answer.append(0)
    return answer

def calc(bNum):
    if len(bNum) <= 1:
        return True
    mid = len(bNum) // 2
    root = bNum[mid]
    subL = bNum[:mid]
    subR = bNum[mid+1:]
    if root == '0':
        if '1' in subL or '1' in subR:
            return False
    return calc(subL) and calc(subR)