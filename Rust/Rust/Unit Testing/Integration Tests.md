1. Integration tests are stored in a top level "tests" directory
2. Integration tests can't import items from binary crate directly. So it's common to have a small binary crate and majority of other stuff in the library crate.

#### Running a specific integration test ( e.g. /tests/order_test.rs)
```rust
cargo test --test order_test
```