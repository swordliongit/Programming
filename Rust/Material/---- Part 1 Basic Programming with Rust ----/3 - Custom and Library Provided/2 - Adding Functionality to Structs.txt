// -------------------------------------------
// 	Adding Functionality to Structs
// -------------------------------------------

struct Car {
    owner: String,
    year: u32,
    fuel_level: f32,
    price: u32,
}
impl Car {
    fn monthly_insurance() -> u32 {
        123
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

    fn display_car_info(&self) {
        println!(
            "Owner: {}, Year: {}, Price: {}",
            self.owner, self.year, self.price
        );
    }

    fn refuel(&mut self, gallons: f32) {
        self.fuel_level += gallons;
    }

    fn sell(self) -> Self {
        self
    }
}

fn main() {
    let mut my_car = Car {
        owner: String::from("ABC"),
        year: 2010,
        fuel_level: 0.0,
        price: 5_000,
    };

    my_car.display_car_info();
    // display_car_info(&my_car);

    my_car.refuel(10.5);
    let new_owner = my_car.sell();
    // my_car.refuel(10.5);

    let new_car = Car::new("XYZ".to_string(), 2020);
}
