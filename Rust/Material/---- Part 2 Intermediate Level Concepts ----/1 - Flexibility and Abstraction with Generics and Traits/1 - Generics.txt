// -------------------------------------------
// 			Generics
// -------------------------------------------

struct Point<T, U> {
    x: T,
    y: U,
}

impl<T, U> Point<T, U> {
    fn new(x: T, y: U) -> Point<T, U> {
        Point { x, y }
    }
}

impl Point<i32, i32> {
    fn printing(&self) {
        println!("The values of the coordinates are {}, {}", self.x, self.y);
    }

    fn new_1(x: i32, y: i32) -> Point<i32, i32> {
        Point { x, y }
    }
}

impl Point<f64, f64> {
    fn printing(&self) {
        println!("The values of the coordinates are {}, {}", self.x, self.y);
    }
}

fn add_points<T, U>(p1: &Point<T, U>, p2: &Point<T, U>) -> Point<T, U> {
    unimplemented!();
}

fn add_points_i32(p1: &Point<i32, i32>, p2: &Point<i32, i32>) -> Point<i32, i32> {
    unimplemented!();
}

fn add_points_f64(p1: &Point<f64, f64>, p2: &Point<f64, f64>) -> Point<f64, f64> {
    unimplemented!();
}

fn main() {
    let origin = Point::new(0, 0);
    let p1 = Point::new(1.0, 4.0);

    let p2 = Point::new(5, 5.0);

    origin.printing();
    // p1.printing();

    add_points(&origin, &origin); // add_points_i32(&origin, &origin);
    add_points(&p1, &p1); // add_points_f64(&p1, &p1);
}
