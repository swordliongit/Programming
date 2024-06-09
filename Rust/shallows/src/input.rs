//
//
//
//

fn main() {
    // positional arguments
    let n1 = 10;
    let n2 = 15;
    println!("{2} + {1} equals to {0}", n1 + n2, n1, n2);

    // named arguments
    println!(
        "{game} is one of the best RPGs ever made",
        game = "No Rest for the Wicked"
    );

    // input
    let mut n = String::new();
    std::io::stdin()
        .read_line(&mut n)
        .expect("Failed to read input!");

    let n: i64 = n.trim().parse().expect("Invalid Input!");
    println!("{n}");

    // Conventions
    let x = 40_000_000;
    println!("{x}");

    static MSG: &str = "Welcome home my child"; // All references to a static refers to the same memory location, 1 instance of the value
    const PI: f32 = 3.14; // constants are inlined and do not occupy a specific location in memory

    let a = PI;
    let b = PI;

    let c = MSG;
    let d = MSG;
}
