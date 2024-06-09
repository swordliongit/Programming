//
//
//
//
//
//
//

use std::vec;

fn main() {
    // &str and String
    let fixed_str = "Fixed length string"; // string slice
    let mut flexible_str = String::from("This string will grow");

    flexible_str.push('d');
    println!("{flexible_str}");
    // Arrays
    let mut array_1 = [4, 5, 6, 7, 8];
    let num = array_1[0];

    println!("{:?}", array_1); // format specifier for compound data types
    let array_2 = [0; 10]; // array with 10 elements initialized to 0

    // Vectors
    let vec_1: Vec<i32> = vec![1, 2, 3, 10, 39];
    let num = vec_1[3];
    println!("{:?}", vec_1);

    // Tuples
    let my_info = ("Salary", 40000, "Age", 40);
    let salary_value = my_info.1;
    let (salary, salary_value, age, age_value) = my_info;
    print!("{salary}, {salary_value}, {age}, {age_value}");

    // Unit type, related to Tuple
    let unit = ();
}
