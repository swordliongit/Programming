//
//
// Borrowing
//
//
fn main() {
    let mut vec_1 = vec![1, 10, 50];
    let ref1 = &vec_1;
    let ref2 = &vec_1;
    let ref3 = &mut vec_1;
    println!("{:?} {:?}", ref1, ref2);
}
