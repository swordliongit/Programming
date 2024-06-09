// Problem 3: Fix the code so that it compiles.

fn main() {
    let str1 = {
        let str1 = generate_string();
        str1
    };
    let str2 = str1; // Something wrong with this line
}

fn generate_string() -> String {
    let some_string = String::from("I will generate a string");
    some_string
}
