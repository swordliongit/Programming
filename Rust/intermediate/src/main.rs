//
//
//
//      GENERICS
//

struct Point<T, U> {
    x: T,
    y: U,
}

impl<T, U> Point<T, U> {
    fn new(x: T, y: U) -> Point<T, U> {
        Point { x, y }
    }
}

// Specialization
impl Point<i32, i32> {
    fn print_coord(&self) {
        println!("Point: {}, {}", self.x, self.y);
    }
}

fn main() {
    let origin = Point::new(0, 0);
    let p1 = Point { x: 1.2, y: 3.5 };

    let p2 = Point { x: 12.0, y: 7 };
    println!("Hello, world!");
}
