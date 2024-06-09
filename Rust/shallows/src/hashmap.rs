//
//
//
//
//
// HASH MAP
use std::collections::HashMap;

fn main() {
    // let mut person: HashMap<&str, i32> = HashMap::new();
    // person.insert("Sword", 26);
    // person.insert("Lion", 30);
    // person.insert("Contra", 35);

    // println!("The age is {:?}", person.get("Lion").unwrap());

    // if person.contains_key("Contra") {
    //     println!("Contra exists in the HashMap");
    // }

    // match person.get("Sword") {
    //     Some(value) => println!("The value exists: {}", value),
    //     None => println!("The value doesn't exist"),
    // }

    // for (name, person) in &person {
    //     println!("The person \"{}\" is {} years old", name, person);
    // }

    // // Value updates
    // let mut likes: HashMap<&str, &str> = HashMap::new();

    // likes.insert("Sword", "Orange");
    // likes.insert("Sword", "Watermelon"); // Overwritten

    // // print!("{:?}", likes); // {"Sword": "Watermelon"}

    // likes.entry("Sword").or_insert("Orange");
    // likes.entry("Sword").or_insert("Watermelon"); // Not updated because "Sword" exists

    // print!("{:?}", likes); // {"Sword": "Orange"}
    let some_vec = vec![2, 2, 5, 6, 2, 8, 2, 2, 2, 5, 1, 10, 6, 2, 8];
    let mut freq_map: HashMap<i32, u32> = HashMap::new();

    for i in &some_vec {
        let freq = freq_map.entry(*i).or_insert(0);
        *freq += 1;
    }

    println!("{:?}", freq_map);
}
