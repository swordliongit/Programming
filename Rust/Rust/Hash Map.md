```rust
use std::collections::HashMap;

fn main() {
    let mut person: HashMap<&str, i32> = HashMap::new();
    person.insert("Sword", 26);
    person.insert("Lion", 30);
    person.insert("Contra", 35);
}
```

## Getting a value, get()
```rust
println!("The age is {:?}", person.get("Lion").unwrap());
// unwrap() Returns the contained `Ok` value, consuming the `self` value.
```

## Checking for a key, contains_key()
```rust
if person.contains_key("Contra") {
	println!("Contra exists in the HashMap");
}
```

```rust
match person.get("Sword") {
	Some(value) => println!("The value exists: {}", value),
	None => println!("The value doesn't exist"),
}
```

## Iterating over a HashMap
```rust
for (name, person) in &person {
	println!("The person \"{}\" is {} years old", name, person);
}
```

## Updating values, insert() and entry()
```rust
let mut likes: HashMap<&str, &str> = HashMap::new();

likes.insert("Sword", "Orange");
likes.insert("Sword", "Watermelon"); // Overwritten
print!("{:?}", likes); // {"Sword": "Watermelon"}
```

```rust
let mut likes: HashMap<&str, &str> = HashMap::new();

likes.entry("Sword").or_insert("Orange");
likes.entry("Sword").or_insert("Watermelon"); // Not updated because "Sword" exists

print!("{:?}", likes); // {"Sword": "Orange"}
```

## Examples
---

## Program to check frequency of Vector elements
```rust
use std::collections::HashMap;

fn main() {
	let some_vec = vec![2, 2, 5, 6, 2, 8, 2, 2, 2, 5, 1, 10, 6, 2, 8];
	let mut freq_map: HashMap<i32, u32> = HashMap::new();
	
	for i in &some_vec {
		let freq = freq_map.entry(*i).or_insert(0);
		*freq += 1;
	}
	
	println!("{:?}", freq_map);
}
```