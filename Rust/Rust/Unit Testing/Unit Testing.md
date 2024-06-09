1. #[cfg(test)] attribute to indicate this code should only run in cargo test
2. #[test] to mark the function to test
3. assert macros are used to test for equality
4. Run ==cargo test==


1. Panic is created if an assertion fails
2. It's good to create a test module for testing purposes. But test functions can be outside the #[cfg(test)] attribute.
3. test functions can access private items
```rust
fn p_func( {
....
}

mod tests {
	#[test]
	fn test_func() {
		p_func();
	}
}
```

---

```rust
// Asserts that two expressions are equal to each other (using PartialEq).
assert_eq!(
            larger_circle.contains(&smaller_circle),
            true,
            "Custom failure message" // optional argument
        );
        
// Asserts that two expressions are not equal to each other (using PartialEq).
assert_ne!(larger_circle.contains(&smaller_circle),
            true);

// Asserts that a boolean expression is `true` at runtime.
assert!(larger_circle.contains(&smaller_circle));
```

*lib.rs:*
```rust
mod shapes {
    pub struct Circle {
        radius: f32,
    }

    impl Circle {
        pub fn new(radius: f32) -> Circle {
            Circle { radius }
        }

        pub fn contains(&self, other: &Circle) -> bool {
            self.radius > other.radius
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn larger_circle_should_contain_smaller() {
        let larger_circle = shapes::Circle::new(5.0);
        let smaller_circle = shapes::Circle::new(2.0);
        assert_eq!(larger_circle.contains(&smaller_circle), true);
    }
}
```

# Assert with Result and Error Propagation

## ? Operator
1. It unpacks the Result if OK
1. It returns the error if not, calling From::from on the error value to potentially convert it to another type.

```rust
fn halves_if_even(i: i32) -> Result<i32, Error> {
    if i % 2 == 0 {
        Ok(i / 2)
    } else {
        Err(/* something */)
    }
}

fn do_the_thing(i: i32) -> Result<i32, Error> {
    let i = match halves_if_even(i) {
        Ok(i) => i,
        Err(e) => return Err(e),
    };

    // use `i`
}
```

```rust
fn do_the_thing(i: i32) -> Result<i32, Error> {
    let i = halves_if_even(i)?;

    // use `i`
}
```


## Assert Result
```rust
....
		pub fn new_with_result(radius: f32) -> Result<Circle, String> {
            if radius >= 0.0 {
                Ok(Circle { radius })
            } else {
                Err(String::from("Radius should be positive integer"))
            }
        }
....

	#[test]
    fn should_not_create_circle() -> Result<(), String> {
        // ? : if Err variant is received, it makes the function return it,
        // if Ok variant is received, it passes control to the next statement.
        let some_circle = shapes::Circle::new_with_result(-2.0)?;
        Ok(())
    }
```


# Panic Testing


- ==#[should_panic]== attribute tests panics, test passes if the function panics.
- ==panic!() ==macro launches a panic

## Example:
new() constructor accepts negative values so it will not panic, resulting in failed test
```rust
mod shapes {

    pub struct Circle {
        radius: f32,
    }

    impl Circle {
        pub fn new_with_negative_check(radius: f32) -> Circle {
            match radius {
                ..=0.0 => panic!("radius should be positive"),
                _ => Circle { radius },
            }
        }
....



#[test]
#[should_panic]
fn should_not_create_and_panic() {
	let some_circle = shapes::Circle::new(-3.0);
}
```

## Panic Test with Custom message

```rust
#[test]
#[should_panic(expected = "wrong expected string")]
fn should_not_create_and_panic_msg() {
	let some_circle = shapes::Circle::new_with_negative_check(-3.0);
}
```

After cargo test:
```
---- tests::should_not_create_and_panic_msg stdout ----
thread 'tests::should_not_create_and_panic_msg' panicked at src\lib.rs:22:27:
radius should be positive
note: panic did not contain expected string
      panic message: `"radius should be positive"`,
 expected substring: `"wrong expected string"`

failures:
    tests::should_not_create_and_panic_msg
```

---

# Unit Testing Control


- #### Selective Testing
	- Use ==cargo test --lib== to only test for the library crate and not the other ones ( e.g. main.rs )

- #### Functions don't output anything in tests by default ( e.g. println! ). Use to show output:
	==cargo test --lib -- --show-output==
	
- #### Running a specific test:
	==cargo test --lib "test_function_name"==
	
- #### Running partial named tests:
	==cargo test --lib "test_deploy_"== -> all the test functions that have test_deploy_ in the name will be tested.

- #### Ignoring specific tests ( e.g. a long running function )
```rust
#[test]
#[ignore]
fn huge_long_running_func() {
	// runs for hours
}
```

output of cargo test --lib:
```
running 6 tests
test tests::huge_long_running_func ... ignored
test tests::larger_circle_should_contain_smaller ... ok
test tests::should_not_create_and_panic - should panic ... ok
test tests::should_not_create_and_panic_msg - should panic ... ok
test tests::should_not_create_circle ... ok
test tests::smaller_circle_should_not_contain_larger ... ok
```


- #### Running the ignored tests: ==cargo test --lib -- --ignored==


# Example Unit Tests

Flow : When testing; if divides_correctly returns Err, test fails with the Err message outputting, if the result is not 5, the test fails too, with the assert_eq!, otherwise returns Ok

```rust
fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        return Err("Cannot divide by zero".to_string());
    }
    Ok(a / b)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn divides_correctly() -> Result<(), String> {
        let result = divide(10, 0)?;
        assert_eq!(result, 5);
        Ok(())
    }
}
```

---


[[Integration Tests]]
[[Benchmark Testing]]