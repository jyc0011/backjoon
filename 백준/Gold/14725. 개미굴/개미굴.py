import sys

input = sys.stdin.readline

def insert(trie, foods):
    node = trie
    for food in foods:
        if food not in node:
            node[food] = {}
        node = node[food]

def dfs(trie, depth):
    for food in sorted(trie.keys()):
        print("--" * depth + food)
        dfs(trie[food], depth + 1)

N = int(input().strip())
trie = {}
for _ in range(N):
    data = input().strip().split()
    k = int(data[0])
    foods = data[1:]
    insert(trie, foods)
    
dfs(trie, 0)