## String Slice and String
```rust
let str = String::new();
let str2 = String::from("Test String");

let fixed_str = "Fixed length string"; // string slice
let mut flexible_str = String::from("This string will grow");
```

### Concatenate Two Strings, push_str()
```rust
let mut str1 = String::from("Hello ");
str1.push_str("World");

println!("{:?}", str1); // Hello World
```

---

## Vector
```rust
let vec: Vec<i32> = Vec::new();
let vec = vec![1, 5, 10, 29];
```

### Useful methods
```rust
// Sum of values
let sum = vec.iter().sum();
```

---

## Tuple
```rust
let my_info = ("Salary", 40000, "Age", 40);

let salary_value = my_info.1;

let (salary, salary_value, age, age_value) = my_info;

print!("{salary}, {salary_value}, {age}, {age_value}");
```

## Unit Type
```rust
// Unit type, related to Tuple
let unit = ();
```

---
