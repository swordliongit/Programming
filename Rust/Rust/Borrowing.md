1. At any time, you can have either ==one mutable== reference or ==any number of immutable== references.
2. References must always be valid.

--- 

1. clone() takes up heap space and transfering ownership is not efficient so we need to borrow, refer to values instead.
2. Can't borrow immutable values as mutable.
3. Mutable references are moved, Immutable references are copied.

```rust
fn main() {
    let mut vec_1 = vec![1, 10, 50];
    let ref1 = &vec_1; // immutable borrow
    let ref3 = &mut vec_1; // mutable borrow  -> error
}
```

```rust
fn main() {
    let vec_1 = vec![1, 200, 344];
    let ref_1 = &vec_1;
    borrows_vector(ref_1);
}

fn borrows_vector(vec: &Vec<i32>) { // vector is borrowed, no extra heap space taken, more efficient.
    println!("{:?}", vec);
}
```

## Dereferencing
```rust
fn main() {
    let mut data = 100;
    let ref_1 = &mut data;
    let copied_data = *ref_1; // copied. Works on stack allocated values only
    *ref_1 = 15; // copied_data not affected
}
```

## Can't move out of mutable references
```rust
fn main() {
    let mut heap_data = vec![1, 200, 232];
    let ref_2 = &mut heap_data;
    let copied_heap_data = *ref_2; // doesn't work
    let copied_heap_data = ref_2.clone(); // works
}
```

## Multiple Redirection
```rust
let s1: String = String::from("Hello");
let r1: &String = &s1;
let r2: &&String = &r1;
let r3: &&&String = &r2;
println!("{}", { ***r3 == "Hello".to_string() }); // true
```