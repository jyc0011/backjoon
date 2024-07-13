use std::io::{self, BufRead};

fn calc(n: usize, k: usize, coins: Vec<usize>) -> usize {
    let mut dp = vec![0; k + 1];
    dp[0] = 1;

    for &coin in &coins {
        for amount in coin..=k {
            dp[amount] += dp[amount - coin];
        }
    }

    dp[k]
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let line = input.next().unwrap().unwrap();
    let mut line_iter = line.split_whitespace();
    let n: usize = line_iter.next().unwrap().parse().unwrap();
    let k: usize = line_iter.next().unwrap().parse().unwrap();

    let mut coins = Vec::with_capacity(n);
    for _ in 0..n {
        let coin = input.next().unwrap().unwrap().trim().parse().unwrap();
        coins.push(coin);
    }

    let result = calc(n, k, coins);
    println!("{}", result);
}