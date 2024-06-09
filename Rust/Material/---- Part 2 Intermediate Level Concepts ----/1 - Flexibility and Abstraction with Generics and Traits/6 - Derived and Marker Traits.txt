// -------------------------------------------
// 			Derived Traits
// 			Marker Traits
// -------------------------------------------

trait Properties: PartialEq + Default + Clone {}
#[derive(Debug, PartialEq, Default, Clone)]
struct Student {
    name: String,
    age: u8,
    sex: char,
}
impl Properties for Student {}
fn main() {
    let s_1 = Student {
        name: String::from("ABC"),
        age: 35,
        sex: 'M',
    };

    let s_2 = Student {
        name: String::from("XYZ"),
        age: 40,
        sex: 'M',
    };

    println!("Student: {:?}", s_1);
    println!("s_1 and s_2 are equal: {}", s_1 == s_2);
}
