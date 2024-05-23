// 11654
use std::io::{self, Write};

fn main() {
    let mut s = String::new();
    io::stdout().flush().unwrap(); // 버퍼 비우기

    io::stdin().read_line(&mut s).unwrap();

    let c = s.trim(); // 앞뒤 공백제거 method

    if let Some(ch) = c.chars().next() {
        println!("{}", ch as u8); // char변수를 u8변수로 변환
    } else {
        println!("변환에 실패했습니다.");
    }
}