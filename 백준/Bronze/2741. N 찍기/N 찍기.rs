use std::io;
use std::fmt::Write;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();
    let mut result = String::new();
    for i in 1..=n {
        writeln!(result, "{}", i).unwrap();
    }
    print!("{}", result);
}