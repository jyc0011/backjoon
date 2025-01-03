use std::collections::BinaryHeap;
use std::cmp::Reverse;
use std::io::{self, BufRead};

fn min_(n: usize, card: Vec<usize>) -> usize {
    let mut heap = BinaryHeap::new();
    for &pack in &card {
        heap.push(Reverse(pack));
    }
    let mut total_ = 0;
    while heap.len() > 1 {
        let Reverse(first) = heap.pop().unwrap();
        let Reverse(second) = heap.pop().unwrap();
        total_ += first + second;
        heap.push(Reverse(first + second));
    }
    
    total_
}

fn main() {
    let stdin = io::stdin();
    let mut input = String::new();
    
    stdin.read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    
    let mut card = Vec::with_capacity(n);
    for _ in 0..n {
        input.clear();
        stdin.read_line(&mut input).unwrap();
        let pack: usize = input.trim().parse().unwrap();
        card.push(pack);
    }
    
    let result = min_(n, card);
    println!("{}", result);
}