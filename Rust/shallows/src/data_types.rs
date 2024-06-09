//
//
//
//
//
//
//
fn main() {
    // Unsigned integers
    let unsigned_num: u8 = 5; // u16, u32, u64, u128

    // Signed integers
    let signed_num: i8 = 5; // i16, i32, i64, i128

    // Floating point numbers
    let float_num: f32 = 5.0; // f64 ( default )

    // Platform specific integers
    let arch_1: usize = 5;
    let arch_2: isize = 5;

    // Characters
    let char: char = 'a';

    // Boolean
    let b: bool = true;

    // Type aliasing
    type Age = u8;
    let peter_age: Age = 42;
    // Type conversion
    let a = 10;
    let b = a as f64;
}
