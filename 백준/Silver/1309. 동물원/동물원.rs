use std::io::{self, BufRead};

fn calc(n: usize) -> usize {
    const MOD: usize = 9901;
    
    let mut dp = vec![vec![0; 3]; n + 1];
    
    dp[1][0] = 1;
    dp[1][1] = 1;
    dp[1][2] = 1;
    
    for i in 2..=n {
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD;
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD;
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD;
    }
    
    (dp[n][0] + dp[n][1] + dp[n][2]) % MOD
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();
    
    let n: usize = input.next().unwrap().unwrap().trim().parse().unwrap();
    
    let result = calc(n);
    println!("{}", result);
}