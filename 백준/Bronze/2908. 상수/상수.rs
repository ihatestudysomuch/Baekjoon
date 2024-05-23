use std::io::{self, Write};

fn main() {
    let mut s = String::new();
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut s)
        .expect("문자열을 입력받지 못했습니다.");

    let n: Vec<u32> = s
        .trim() //공백 제거
        .split_whitespace() // 공백을 기준으로 문자열을 나눔
        .map(|s| s.chars().rev().collect::<String>().parse().unwrap())
        // 아직 클로저 안배움.. chars()는 문자로 변환, rev()는 문자열 뒤집기
        .collect(); //Vec<u32>로 반환

    let max = n.iter().max().unwrap(); //Vec를 순회하는 iter값 반환
    print!("{}", max);
}
