//
//
// ENUM
//
//

enum Days {
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday,
}

enum TravelType {
    Car(f32),
    Train(f32),
    Plane(f32),
}

impl TravelType {
    fn travel_compensation(&self) -> f32 {
        match self {
            TravelType::Car(miles) => miles * 2.0,
            TravelType::Train(miles) => miles * 3.0,
            TravelType::Plane(miles) => miles * 5.0,
        }
    }
}

fn main() {
    let day = Days::Saturday;

    let car = TravelType::Car(100.0);
    println!(
        "Compensation for the customer: {}",
        car.travel_compensation()
    );
}
