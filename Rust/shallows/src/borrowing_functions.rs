//
//
//
//
// //
fn main() {
    let mut vec_1 = vec![1, 200, 344];
    let ref_1 = &vec_1;
    borrows_vector(ref_1);
    // let ref_2 = &mut vec_1;
    // let vec_1 = transfer_ownership(vec_1);
    mutate_vector(&mut vec_1);
    println!("{:?}", vec_1);
}

// immutable borrow
fn borrows_vector(vec: &Vec<i32>) {
    println!("{:?}", vec);
}

// move
fn transfer_ownership(mut vec: Vec<i32>) -> Vec<i32> {
    vec.push(1000);
    vec
}

// mutable borrow
fn mutate_vector(vec: &mut Vec<i32>) {
    vec.push(1000);
}

fn move_ownership() -> Vec<i32> {
    let vec = vec![1, 100, 20];
    vec.clone()
}
