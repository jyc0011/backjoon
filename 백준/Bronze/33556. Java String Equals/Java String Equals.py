import sys

input=sys.stdin.readline

def equals(A,B):
    if A==B:
        return 'true'
    return 'false'

def equalsIgnoreCase(A,B):
    if A.lower()==B.lower():
        return 'true'
    return 'false'

def isNull(a):
    if a=='null':
        return True
    return False

A=input().rstrip()
B=input().rstrip()

if isNull(A):
    print('NullPointerException')
    print('NullPointerException')
    sys.exit(0)
else:
    if isNull(B):
        B=''
    print(equals(A,B))
    print(equalsIgnoreCase(A,B))