use std::collections::VecDeque;
use std::io::{self, BufRead};

fn bfs(x: usize, y: usize, team: char, f: &Vec<Vec<char>>, visited: &mut Vec<Vec<bool>>, m: usize, n: usize) -> usize {
    let mut queue = VecDeque::new();
    queue.push_back((x, y));
    visited[x][y] = true;
    let mut count = 1;
    let d = [(-1isize, 0isize), (1, 0), (0, -1), (0, 1)];
    while let Some((cx, cy)) = queue.pop_front() {
        for (dx, dy) in &d {
            let nx = cx as isize + dx;
            let ny = cy as isize + dy;
            if nx >= 0 && nx < m as isize && ny >= 0 && ny < n as isize {
                let nx = nx as usize;
                let ny = ny as usize;
                if !visited[nx][ny] && f[nx][ny] == team {
                    visited[nx][ny] = true;
                    queue.push_back((nx, ny));
                    count += 1;
                }
            }
        }
    }
    count
}

fn main() {
    let stdin = io::stdin();
    let mut input = String::new();
    stdin.read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap(); // N
    let m: usize = iter.next().unwrap().parse().unwrap(); // M
    let mut f = Vec::with_capacity(m);
    for _ in 0..m {
        input.clear();
        stdin.read_line(&mut input).unwrap();
        let line = input.trim().chars().collect::<Vec<char>>();
        f.push(line);
    }
    let mut visited = vec![vec![false; n]; m];
    let mut my = 0;
    let mut enemy = 0;
    for i in 0..m {
        for j in 0..n {
            if !visited[i][j] {
                match f[i][j] {
                    'W' => {
                        let count = bfs(i, j, 'W', &f, &mut visited, m, n);
                        my += count * count;
                    }
                    'B' => {
                        let count = bfs(i, j, 'B', &f, &mut visited, m, n);
                        enemy += count * count;
                    }
                    _ => {}
                }
            }
        }
    }
    println!("{} {}", my, enemy);
}