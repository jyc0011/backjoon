use std::io;

fn check(board: &Vec<Vec<i32>>) -> i32 {
    let mut bingo_cnt = 0;

    for row in board {
        if row.iter().sum::<i32>() == 0 {
            bingo_cnt += 1;
        }
    }

    for col in 0..5 {
        if (0..5).map(|row| board[row][col]).sum::<i32>() == 0 {
            bingo_cnt += 1;
        }
    }

    if (0..5).map(|i| board[i][i]).sum::<i32>() == 0 {
        bingo_cnt += 1;
    }
    if (0..5).map(|i| board[i][4 - i]).sum::<i32>() == 0 {
        bingo_cnt += 1;
    }

    bingo_cnt
}

fn main() {
    let stdin = io::stdin();
    let mut board = vec![vec![0; 5]; 5];
    for i in 0..5 {
        let mut input = String::new();
        stdin.read_line(&mut input).unwrap();
        let numbers: Vec<i32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
        for j in 0..5 {
            board[i][j] = numbers[j];
        }
    }

    let mut calls = Vec::new();
    for _ in 0..5 {
        let mut input = String::new();
        stdin.read_line(&mut input).unwrap();
        let numbers: Vec<i32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
        calls.extend(numbers);
    }

    let mut position_map = std::collections::HashMap::new();
    for i in 0..5 {
        for j in 0..5 {
            position_map.insert(board[i][j], (i, j));
        }
    }

    for (count, &call) in calls.iter().enumerate() {
        if let Some(&(x, y)) = position_map.get(&call) {
            board[x][y] = 0;

            if check(&board) >= 3 {
                println!("{}", count + 1);
                break;
            }
        }
    }
}