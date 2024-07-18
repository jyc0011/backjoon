use std::io::{self, BufRead};

fn calc(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
    let mut l = 0;
    let mut r = 0;
    let mut m = Vec::with_capacity(a.len() + b.len());
    
    while l < a.len() && r < b.len() {
        if a[l] <= b[r] {
            m.push(a[l]);
            l += 1;
        } else {
            m.push(b[r]);
            r += 1;
        }
    }
    
    while l < a.len() {
        m.push(a[l]);
        l += 1;
    }
    
    while r < b.len() {
        m.push(b[r]);
        r += 1;
    }
    
    m
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();
    
    let dims = input.next().unwrap().unwrap();
    let mut dims_iter = dims.split_whitespace();
    let _n: usize = dims_iter.next().unwrap().parse().unwrap();
    let _m: usize = dims_iter.next().unwrap().parse().unwrap();
    
    let a_line = input.next().unwrap().unwrap();
    let a: Vec<i32> = a_line.split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    
    let b_line = input.next().unwrap().unwrap();
    let b: Vec<i32> = b_line.split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let res = calc(a, b);
    
    for val in res {
        print!("{} ", val);
    }
    println!();
}