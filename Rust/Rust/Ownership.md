1. Each value has a variable that is its "owner".
2. A value can have only one owner at a time.
3. If the owner goes out of scope, the value is cleaned up.
4. All primitives are stored on Stack. No part in Heap, so there's no moving of values but instead copies are made.
5. Compound types are part Stack part Heap so they are moved by default.


```rust
fn main() {
    let s1 = String::from("hello world");
    let s2 = s1; 
    println!("{s1}"); // Error, s1 was moved
}
```

## s1 in memory:

![[Screenshot 2024-05-31 114325.png]]

## s1 gets deleted after moving the value to s2:
![[Screenshot 2024-05-31 114311.png]]

## Copying ( deep copy )

```rust
fn main() {
    let s1 = String::from("hello world");
    let s2 = s1.clone();
    println!("{s1}"); // works 
}
```

![[Screenshot 2024-05-31 114606.png]]