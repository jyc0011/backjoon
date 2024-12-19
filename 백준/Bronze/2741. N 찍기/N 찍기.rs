use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();
    let result: String = (1..=n).map(|i| i.to_string()).collect::<Vec<String>>().join("\n");
    println!("{}", result);
}