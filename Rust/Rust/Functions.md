1. Semicolon omitted return values must be the last statement in the function. To return early, we must use the ==return== keyword.

```rust
fn mult(num1: i32, num2: i32) -> i32 {
	return 45; // early return
    println!("Multiplying numbers...");
    num1 * num2
}
```