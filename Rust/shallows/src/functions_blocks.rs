//
//
//
//
//

fn main() {
    func("hello world");
    let str = "Fixed string";
    func(str);
    let res = mult(5, 10);
    println!("Multiplication result: {res}");

    let (mult, sum, subt, div) = get_math(20, 5);
    println!("{:?}", get_math(10, 5));

    // Code blocks
    let name = {
        let fname = "Sword";
        let lname = "Lion";
        format!("{fname} {lname}")
    };
    println!("{name}");
}

fn func(s: &str) {
    println!("{s}");
}

fn mult(num1: i32, num2: i32) -> i32 {
    return 45;
    println!("Multiplying numbers...");
    num1 * num2
}

fn get_math(num1: i32, num2: i32) -> (i32, i32, i32, i32) {
    (num1 * num2, num1 + num2, num1 - num2, num1 / num2)
}
