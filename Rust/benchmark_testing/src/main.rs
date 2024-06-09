fn main() {
    let mut s = String::new();

    std::io::stdin()
        .read_line(&mut s)
        .expect("Failed to read Input");
    let inp: i32 = s.trim().parse().expect("Invalid Input");

    let anonvar = |i| -> i32 { inp * i };
    println!("{:?}", anonvar(10));
}
