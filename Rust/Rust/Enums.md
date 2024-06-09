1. Enum values are called ==variants==


```rust
enum Days {
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday,
}

fn main() {
    let day = Days::Saturday;
}
```

## Associated Values of Variants

```rust
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
    let car = TravelType::Car(100.0);
    println!(
        "Compensation for the customer: {}",
        car.travel_compensation()
    );
}
```


## Option

- In Rust preload, so it's auto-loaded in every program
- it's used in place of null in other languages
- Use if you want to represent presence or absence of value

```rust
// enum Option<T> {
//     None,
//     Some(T),
// }
```

```rust
struct Student {
    name: String,
    grade: Option<u32>,
}

fn main() {
    let student_db = vec![
        Student {
            name: String::from("Sword"),
            grade: Some(78),
        },
        Student {
            name: String::from("Lion"),
            grade: Some(90),
        },
        Student {
            name: String::from("Contra"),
            grade: None,
        },
    ];
}
```


## Destructuring Option Variants - if let
- Good if we care about only 1 variant and discard all others

```rust
let student_grade = get_grade(&student_name, &student_db); // can return either None or Some()

match student_grade {
	Some(grade) => println!("{}'s grade is {}", student_name, grade),
	None => {}
}

// identical but cleaner code
if let Some(grade) = student_grade {
	println!("{}'s grade is {}", student_name, grade);
}
```

## Result

- Use it to represent success or failure of an operation

```rust
enum Result<E, T> {
    Ok(T),
    Err(E),
}
```

```rust
fn check_grade(student_name: &String, student_db: &Vec<Student>) -> Result<Option<u32>, String> {
    for student in student_db {
        if student.name == *student_name {
            return Ok(student.grade);
        }
    }
    Err(String::from("Student not found!"))
}
```