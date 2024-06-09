//Problem 1: Modify the code by eliminating all the let statements

use core::f64;

struct Car {
    owner: String,
    year: u32,
    fuel_level: f64,
    price: u32,
}

impl Car {
    fn monthly_insurance() -> u32 {
        200
    }

    fn selling_price(&self) -> u32 {
        self.price + Car::monthly_insurance()
    }

    fn new(name: String, year: u32) -> Self {
        Self {
            owner: name,
            year: year,
            fuel_level: 0.0,
            price: 0,
        }
    }

    fn display_info(&self) {
        println!(
            "Owner: {}, Year: {}, Price: {}, Fuel: {}",
            (*self).owner, // automatic dereference
            self.year,
            self.price,
            self.fuel_level,
        );
    }

    fn refuel(&mut self, gallons: f64) {
        self.fuel_level += gallons;
    }

    fn sell(self) -> Self {
        self
    }
}

fn main() {
    let mut car_1 = Car {
        owner: String::from("Sword"),
        year: 2024,
        fuel_level: 10.0,
        price: 1_500_000,
    };

    car_1.display_info();
    car_1.refuel(20.0);
    car_1.display_info();

    let mut car_2 = car_1.sell();
    car_2.display_info();
    println!("{}", car_2.selling_price());

    let new_car = Car::new("Togg".to_string(), 2024);
    new_car.display_info();
}
