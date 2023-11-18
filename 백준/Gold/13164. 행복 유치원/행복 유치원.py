n, k = map(int, input().split())
height = list(map(int, input().split()))
cost = []

for i in range(n-1):
    cost.append(height[i+1] - height[i])

cost.sort(reverse=True)
cost = cost[k-1:]

print(sum(cost))    