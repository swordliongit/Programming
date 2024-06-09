// Problem 2:

/*
Fix the code below. By solving this problem you will be able to understand
the change of ownership inside a loop
*/

fn main() {
    let mut my_vec = vec![1, 2, 3, 4, 5];
    let mut temp;

    while !my_vec.is_empty() {
        temp = my_vec.clone(); // Something wrong on this line
        println!("Elements in temporary vector are: {:?}", temp);

        if let Some(last_element) = my_vec.pop() {
            // pop() is used to remove an element from the vec
            println!("Popped element: {}", last_element);
        }
    }
}
