//
//
// loop, for, while
//
//

fn main() {
    // labeled loop
    'outer: loop {
        println!("Simplest loop");
        loop {
            println!("Inner loop");
            break 'outer; // exit from the outer loop
        }
    }

    let a = loop {
        break 5; // 5 will be returned
    };

    let vec = vec![1, 10, 100, 1000, 10000];

    for i in vec {
        print!("{i}, ");
    }
    println!();

    let mut num = 0;
    while num < 10 {
        num += 1;
    }
    println!("{num}");
}
