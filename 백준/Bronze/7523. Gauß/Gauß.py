import sys

def sum(num):
	return num * (num + 1) // 2

for i in range(1,int(sys.stdin.readline())+1):
	a, b = map(int, sys.stdin.readline().split())
	print("Scenario #%d:"%(i))
	print(sum(b)-sum(a-1))
	print()