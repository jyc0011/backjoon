use std::io;

fn calc(w: usize, h: Vec<usize>) -> usize {
    if h.is_empty() || h.len() < 3 {
        return 0;
    }
    
    let mut l = 0;
    let mut r = w - 1;
    let mut l_max = h[l];
    let mut r_max = h[r];
    let mut water = 0;
    
    while l < r {
        if l_max < r_max {
            l += 1;
            l_max = l_max.max(h[l]);
            water += l_max.saturating_sub(h[l]);
        } else {
            r -= 1;
            r_max = r_max.max(h[r]);
            water += r_max.saturating_sub(h[r]);
        }
    }
    
    water
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let dims: Vec<usize> = input.trim().split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let _h = dims[0];
    let w = dims[1];

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let heights: Vec<usize> = input.trim().split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let res = calc(w, heights);
    println!("{}", res);
}