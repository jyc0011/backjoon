import sys

input = sys.stdin.readline

N = 1000000
tree_len = 1
while tree_len < N:
    tree_len *= 2
tree = [0] * (2 * tree_len)

def update(tree, sugar_content, n_candy):
    idx = tree_len + sugar_content - 1
    while idx:
        tree[idx] += n_candy
        idx //= 2

def find(tree, nth_node, rank):
    if nth_node >= tree_len:
        print(nth_node - tree_len + 1)
        tree[nth_node] -= 1
        return
    
    left_child_count = tree[2 * nth_node]
    if rank <= left_child_count:
        find(tree, 2 * nth_node, rank)
    else:
        find(tree, 2 * nth_node + 1, rank - left_child_count)
    tree[nth_node] -= 1


tree = [0] * (tree_len << 1)

for _ in range(int(sys.stdin.readline())):
    op, *args = map(int, sys.stdin.readline().split())

    if op == 1:
        rank = args[0]
        find(tree, 1, rank)
    
    else:
        sugar_content, n_candy = args
        update(tree, sugar_content, n_candy)