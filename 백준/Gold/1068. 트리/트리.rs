use std::io;

fn dfs(node: usize, delete_node: usize, tree: &Vec<Vec<usize>>) -> usize {
    if node == delete_node {
        return 0;
    }
    if tree[node].is_empty() || (tree[node].len() == 1 && tree[node][0] == delete_node) {
        return 1;
    }
    let mut leaf_count = 0;
    for &child in &tree[node] {
        leaf_count += dfs(child, delete_node, tree);
    }
    leaf_count
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let parents: Vec<i32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let delete_node: usize = input.trim().parse().unwrap();
    let mut tree = vec![Vec::new(); n];
    let mut root = None;
    for i in 0..n {
        if parents[i] == -1 {
            root = Some(i);
        } else {
            tree[parents[i] as usize].push(i);
        }
    }
    if let Some(root_node) = root {
        if root_node == delete_node {
            println!("0");
        } else {
            let leaf_count = dfs(root_node, delete_node, &tree);
            println!("{}", leaf_count);
        }
    }
}