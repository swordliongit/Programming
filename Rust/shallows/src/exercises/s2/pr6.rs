// Problem 6:

/*
Write a function that implements the logic,
'You can see the movie if you are 17 or older, or if you are 13 or older and have a parent's permission.'
*/

fn can_see_movie(age: i32, permission: bool) -> bool {
    // Write your code here to implement the logic
    age >= 17 || (age >= 13 && permission)
}

fn main() {
    println!("{}", can_see_movie(13, true));
}
