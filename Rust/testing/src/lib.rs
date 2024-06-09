mod shapes {

    pub struct Circle {
        radius: f32,
    }

    impl Circle {
        pub fn new(radius: f32) -> Circle {
            println!("A circle is created!");
            Circle { radius }
        }

        pub fn new_with_result(radius: f32) -> Result<Circle, String> {
            if radius >= 0.0 {
                Ok(Circle { radius })
            } else {
                Err(String::from("Radius should be positive"))
            }
        }

        pub fn new_with_negative_check(radius: f32) -> Circle {
            match radius {
                ..=0.0 => panic!("radius should be positive"),
                _ => Circle { radius },
            }
        }

        pub fn contains(&self, other: &Circle) -> bool {
            self.radius > other.radius
        }
    }
}

#[cfg(test)]
mod tests {
    // use shapes::Circle;

    use super::*;

    #[test]
    fn larger_circle_should_contain_smaller() {
        let larger_circle = shapes::Circle::new(5.0);
        let smaller_circle = shapes::Circle::new(2.0);
        assert_eq!(
            larger_circle.contains(&smaller_circle),
            true,
            "Custom failure message"
        );

        // assert_ne!(larger_circle.contains(&smaller_circle), true);
        // assert!(larger_circle.contains(&smaller_circle));
    }

    #[test]
    fn smaller_circle_should_not_contain_larger() {
        let larger_circle = shapes::Circle::new(5.0);
        let smaller_circle = shapes::Circle::new(2.0);
        assert_eq!(smaller_circle.contains(&larger_circle), false);
    }

    #[test]
    fn should_not_create_circle() -> Result<(), String> {
        // ? : if Err variant is received, it makes the function return it,
        // if Ok variant is received, it passes control to the next statement.
        // let some_circle = shapes::Circle::new_with_result(-2.0)?;
        let some_circle = shapes::Circle::new_with_result(5.0)?;

        Ok(())
    }

    #[test]
    #[should_panic]
    fn should_not_create_and_panic() {
        let some_circle = shapes::Circle::new_with_negative_check(-3.0);
    }

    #[test]
    #[should_panic(expected = "radius should be positive")]
    fn should_not_create_and_panic_msg() {
        let some_circle = shapes::Circle::new_with_negative_check(-3.0);
    }

    #[test]
    #[ignore]
    fn huge_long_running_func() {
        {}
    }
}

// pub fn add(left: usize, right: usize) -> usize {
//     left + right
// }

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     fn it_works() {
//         let result = add(2, 2);
//         assert_eq!(result, 4);
//     }
// }
