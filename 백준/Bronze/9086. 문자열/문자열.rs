// 9086
use std::io::{self, Write};

fn main() {
    let mut s = String::new();

    io::stdout().flush().unwrap();

    io::stdin()
        .read_line(&mut s)
        .expect("라인 입력에 실패했습니다");
    let line_numeric = s.trim().parse().expect("라인의 수를 입력하세요");

    for _ in 0..line_numeric {
        s.clear();

        //println!("문자열을 입력하세요");
        io::stdin()
            .read_line(&mut s)
            .expect("문자열 입력에 실패했습니다.");

        let st = s.trim();

        if st.is_empty() {
            println!("s가 비어있습니다.");
        } else {
            let first = st.chars().next().unwrap();
            let last = st.chars().last().unwrap();

            println!("{}{}", first, last);
        }
    }
}

