def solution(n, arr1, arr2):
    result=[]
    for i in range(n):
        comb = format(arr1[i] | arr2[i], 'b').zfill(n)
        map_row = comb.replace('1', '#').replace('0', ' ')
        result.append(map_row)
    return result