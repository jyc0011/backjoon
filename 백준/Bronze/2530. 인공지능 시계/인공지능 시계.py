a, b, c = map(int,input().split())
d = int(input())

x = (3600 * a + 60 *  b + c + d) % 86400

h = x // 3600
m = (x % 3600) // 60
s = (x % 3600) % 60

print(h, m, s)