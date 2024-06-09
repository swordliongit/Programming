// Problem 1: Fix the code below

fn main() {
    let mut some_vec = vec![1, 2, 3];
    some_vec.push(4);
    let first = get_first_element(&some_vec);
    println!("The first number is: {}", first);
}

fn get_first_element(num_vec: &Vec<i32>) -> &i32 {
    &num_vec[0]
}
