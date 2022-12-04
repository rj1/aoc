use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);

    let mut top = 0;
    let mut count = 0;

    for line in reader.lines() {
        let line = line.unwrap();
        if line.is_empty() {
            count = 0;
            continue;
        }

        let current: i32 = line.parse().unwrap();
        count += current;

        if count > top {
            top = count;
        }
    }

    println!("{top}");
}
