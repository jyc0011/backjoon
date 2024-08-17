use std::collections::BinaryHeap;
use std::cmp::Reverse;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = String::new();
    
    stdin.read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();

    let mut node = vec![Vec::new(); n + 1];
    
    for _ in 0..m {
        input.clear();
        stdin.read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();
        let a: usize = iter.next().unwrap().parse().unwrap();
        let b: usize = iter.next().unwrap().parse().unwrap();
        let c: usize = iter.next().unwrap().parse().unwrap();
        node[a].push((b, c));
        node[b].push((a, c));
    }

    let mut heap = BinaryHeap::new();
    heap.push(Reverse((0, 1)));

    let mut dist = vec![usize::MAX; n + 1];
    dist[1] = 0;

    let mut parent = vec![0; n + 1];

    while let Some(Reverse((current_dist, current_node))) = heap.pop() {
        if current_dist > dist[current_node] {
            continue;
        }

        for &(next_node, weight) in &node[current_node] {
            let new_dist = current_dist + weight;
            if new_dist < dist[next_node] {
                dist[next_node] = new_dist;
                parent[next_node] = current_node;
                heap.push(Reverse((new_dist, next_node)));
            }
        }
    }

    println!("{}", n - 1);
    for i in 2..=n {
        println!("{} {}", i, parent[i]);
    }
}