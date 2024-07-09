use std::io; // 입출력 모듈

fn calc(n: usize, s: Vec<i32>) -> i32 { // 함수 정의 n->배열 길이, s->배열
    // dp 변수 선언(let), 변수 변경 예약어(mut)
    // 벡터로 선언해 배열 생성
    // 길이가 n, 값은 0으로 초기화
    let mut dp = vec![0; n];
    // dp 벡터의 첫 번째 값은 벡터 s의 첫 번째 값으로 설정
    dp[0] = s[0];

    for i in 1..n { // 1부터 n-1까지 반복, 간격 미설정(1)
        // dp[i]를 s[i]와 dp[i-1] + s[i] 중
        dp[i] = s[i].max(dp[i - 1] + s[i]); //큰 값으로 설정
    }
    // dp 벡터에서 최대 값을 반환
    // iter : 이터레이터(요소 순회) 리턴
    // unwrap : Option<&i32> -> '&i32'로 변환
    // * : 실제 값(i32 : 32비트 정수 타입)으로 변환
    *dp.iter().max().unwrap()
}

fn main() {

    let mut input = String::new(); // 입력을 받을 문자열 생성
    io::stdin().read_line(&mut input).unwrap(); // 입력 한 라인 읽고 저장
    let n: usize = input.trim().parse().unwrap(); // 문자열->숫자로 변환, n에 저장
    input.clear(); // 비우기

    io::stdin().read_line(&mut input).unwrap();
    let s: Vec<i32> = input // 벡터 s에 저장
        .trim() // 앞 뒤 공백 제거
        .split_whitespace()// 공백을 기준으로 나눔
        .map(|x| x.parse().unwrap()) // i32로 변환
        .collect(); // 벡터 내부에 취합

    // 함수 호출, 결과 출력
    println!("{}", calc(n, s));
}