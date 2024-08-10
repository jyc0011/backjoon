use std::collections::VecDeque;
use std::io;

fn bfs(n: usize, k: usize) -> usize {
    let max_pos = 100_000;
    let mut visited = vec![false; max_pos + 1];
    let mut queue = VecDeque::new();
    queue.push_back((n, 0));
    visited[n] = true;
    while let Some((position, time)) = queue.pop_front() {
        if position == k {
            return time;
        }
        let next_positions = [position.wrapping_sub(1), position + 1, position * 2];   
        for &next_pos in &next_positions {
            if next_pos <= max_pos && !visited[next_pos] {
                visited[next_pos] = true;
                queue.push_back((next_pos, time + 1));
            }
        }
    }
    0
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let k: usize = iter.next().unwrap().parse().unwrap();   
    let result = bfs(n, k);
    println!("{}", result);
}