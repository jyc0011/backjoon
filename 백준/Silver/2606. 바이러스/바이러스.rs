use std::collections::VecDeque;
use std::io::{self, BufRead};

fn bfs(graph: &Vec<Vec<usize>>, start: usize, visited: &mut Vec<bool>) -> usize {
    let mut queue = VecDeque::new();
    queue.push_back(start);
    visited[start] = true;
    let mut count = 0;
    while let Some(node) = queue.pop_front() {
        for &neighbor in &graph[node] {
            if !visited[neighbor] {
                queue.push_back(neighbor);
                visited[neighbor] = true;
                count += 1;
            }
        }
    }
    count
}

fn main() {
    let stdin = io::stdin();
    let mut input = String::new();
    stdin.read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    input.clear();
    stdin.read_line(&mut input).unwrap();
    let m: usize = input.trim().parse().unwrap();
    let mut graph = vec![vec![]; n + 1];

    for _ in 0..m {
        input.clear();
        stdin.read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();
        let a: usize = iter.next().unwrap().parse().unwrap();
        let b: usize = iter.next().unwrap().parse().unwrap();
        graph[a].push(b);
        graph[b].push(a);
    }
    let mut visited = vec![false; n + 1];
    let result = bfs(&graph, 1, &mut visited);
    println!("{}", result);
}