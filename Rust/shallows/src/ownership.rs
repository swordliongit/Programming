use std::{mem::take, vec};

//
//
//
//
fn main() {
    // Ownership
    let s1 = String::from("hello world");
    let s2 = s1.clone();
    println!("{s1}");

    let vec_1 = vec![1, 5, 10];
    take_ownership(vec_1.clone());
    println!("{:?}", vec_1);

    let vec_2 = give_ownership();
    println!("{:?}", vec_2);

    let vec_3 = vec![20, 30, -5];
    let vec_4 = transfer_ownership(vec_3);
    // println!("{:?}", vec_3); // error
    println!("{:?}", vec_4);
}

fn take_ownership(vec: Vec<i32>) {
    println!("{:?}", vec);
}

fn give_ownership() -> Vec<i32> {
    vec![1, 50, 200]
}

fn transfer_ownership(mut vec: Vec<i32>) -> Vec<i32> {
    vec.push(1000);
    vec
}
