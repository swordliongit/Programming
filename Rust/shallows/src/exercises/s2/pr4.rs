// Problem 4:

/*
A palindrome is a word, verse, or sentence that reads the same backward or forward,
such as 'Able was I ere I saw Elba,' or a number like 1881.

Write a function named is_palindrome() that checks whether a given string is a palindrome or not.
The function should take a string as input and return a boolean value indicating whether the string is a palindrome or not.
*/

fn main() {
    let input = String::from("able was I ere I saw elba");
    println!(
        "It is {:?} that the given string is palindrome",
        palindrome(input)
    );
}

fn palindrome(input: String) -> bool {
    /* Your Code here */

    let mut char_list: Vec<char> = Vec::new();
    let mut char_list_reversed: Vec<char> = Vec::new();

    for ch in input.chars() {
        char_list.push(ch);
    }

    for ch in input.chars().rev() {
        char_list_reversed.push(ch);
    }

    // println!("{:?}\n{:?}", char_list, char_list_reversed);

    char_list.eq(&char_list_reversed)
}

// Solution

fn palindrome(input: String) -> bool {
    let mut is_palindrome = true;
    if input.len() == 0 {
        is_palindrome = true;
    } else {
        let mut last = input.len() - 1;
        let mut first = 0;

        let my_vec = input.as_bytes();

        while first < last {
            if my_vec[first] != my_vec[last] {
                is_palindrome = false;
                break;
            }

            first += 1;
            last -= 1;
        }
    }
    is_palindrome
}
