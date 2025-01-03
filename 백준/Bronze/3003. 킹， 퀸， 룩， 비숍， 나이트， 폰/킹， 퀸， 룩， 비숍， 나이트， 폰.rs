use std::io;

fn main() {
    let chess = [1, 1, 2, 2, 2, 8];
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let find: Vec<i32> = input
        .trim()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    
    for i in 0..6 {
        print!("{} ", chess[i] - find[i]);
    }
    println!();
}