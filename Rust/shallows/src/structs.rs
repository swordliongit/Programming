//
//
//
// STRUCT
//
//

use core::f64;

struct Car {
    owner: String,
    year: u32,
    fuel_level: f32,
    price: u32,
}

fn main() {
    let car_1 = Car {
        owner: String::from("Sword"),
        year: 2024,
        fuel_level: 55.0,
        price: 1_500_000,
    };

    let moved_owner = car_1.owner.clone();
    // car_1.owner doesn't exist here
    // println!("{}", car_1.owner); // borrow of moved value, ERROR

    let car_2 = Car {
        owner: String::from("Lion"),
        ..car_1 // car_1 fields are COPIED except the owner
    };

    let car_3 = Car {
        ..car_1 // owner is MOVED to car_3 and other fields are COPIED as they are in stack
    };
    println!("{}", car_1.owner); // borrow of moved value ERROR

    // tuple structs

    let point_2D = (12, 25);
    let point_3D = (23.0, 45.5, 56.7);

    struct Point_2D(i32, i32);
    struct Point_3D(f64, f64, f64);

    let p2D = Point_2D(5, 25);
    let p3D = Point_3D(10.0, 20.0, 30.0);

    let (x, y, z) = (p3D.0, p3D.1, p3D.2);

    // unit struct
    struct ABC;
}
