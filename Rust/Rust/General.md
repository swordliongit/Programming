# 1. ==Code blocks== can be assigned to variables and they can return values
```rust
let name = {
	let fname = "Sword";
	let lname = "Lion";
	format!("{fname} {lname}")
};
```

# 2. Printing Compound types:
```rust
let mut array_1 = [4, 5, 6, 7, 8];
println!("{:?}", array_1);
```


# 3.Input:
```rust
let mut n = String::new();

std::io::stdin()
	.read_line(&mut n)
	.expect("Failed to read input!");

let n: i64 = n.trim().parse().expect("Invalid Input!");
println!("{n}");
```