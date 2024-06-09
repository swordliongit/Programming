// Problem #3: Re-export the items properly so that the code compiles
// Solution:

mod graphics {
    pub use self::display::show_area;
    pub use self::shapes::calculate_area;
    pub mod shapes {
        pub fn calculate_area(radius: f64) -> f64 {
            std::f64::consts::PI * radius * radius
        }
    }
    pub mod display {
        pub fn show_area(shape: &str, area: f64) {
            println!("The area of the {} is: {}", shape, area);
        }
    }
}

use graphics::calculate_area;
use graphics::show_area;
fn main() {
    let radius = 3.0;
    let area = calculate_area(radius);

    show_area("circle", area);
}
