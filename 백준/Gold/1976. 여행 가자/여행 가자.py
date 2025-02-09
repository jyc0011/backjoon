import sys
input = sys.stdin.readline

def union(graph, x, y):
    root1=find(graph, x)
    root2=find(graph, y)
    if root1 != root2:
        graph[root2]=root1
    
def find(graph, x):
    if graph[x] != x:
        graph[x]=find(graph, graph[x])
    return graph[x]

N=int(input())
M=int(input())
root=[i for i in range(N+1)]

for i in range(1, N+1):
    temp=tuple(map(int, input().split()))
    for j in range(1, N+1):
        if temp[j-1]==1:
            union(root, i, j)
            
plan=list(map(int,input().split()))
check = find(root, plan[0])

if all(find(root, temp)==check for temp in plan):
    print("YES")
else:
    print("NO")