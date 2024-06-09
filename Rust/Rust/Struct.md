1. ==self== is the same as ==self: Self==
2. Values of a struct are called ==Fields==

```rust
struct Car {
    owner: String,
    year: u32,
    fuel_level: f32,
    price: u32,
}
```



## Partial Move
```rust
fn main() {
    let car_1 = Car {
        owner: String::from("Sword"),
        year: 2024,
        fuel_level: 55.0,
        price: 1_500_000,
    };

    let moved_owner = car_1.owner; // value pointed to is in heap and other parts in stack
    // car_1.owner doesn't exist here
    println!("{}", car_1.owner); // borrow of moved value, ERROR
    
	let copied_owner = car_1.owner.clone();
	println!("{}", car_1.owner);  // works
}
```


```rust
fn main() {
	let car_1 = Car {
		owner: String::from("Sword"),
		year: 2024,
		fuel_level: 55.0,
		price: 1_500_000,
	};
	
	let car_2 = Car {
		owner: String::from("Lion"),
		..car_1 // car_1 fields are COPIED except the owner
	};

	let car_3 = Car {
        ..car_1 // owner is MOVED to car_3 and other fields are COPIED as they are in stack
    };
    println!("{}", car_1.owner); // borrow of moved value ERROR

}
```

## Passing and returning structs
```rust
struct Fruit {
    apples: i32,
    bananas: i32,
}

fn increase_fruit(fruit: Fruit) -> Fruit {
    Fruit {
        apples: fruit.apples * 2,
        bananas: fruit.bananas * 3,
    }
}

fn new_fruit() -> Fruit {
    Fruit {
        apples: 10,
        bananas: 5,
    }
}

fn print_fruit(fruit: Fruit) {
    println!(
        "You have {} apples and {} bananas",
        fruit.apples, fruit.bananas
    );
}

fn main() {
    // let some_fruit = new_fruit();
    // let updated_fruit = increase_fruit(new_fruit());
    print_fruit(increase_fruit(new_fruit()));
}

```


## Functionality in Structs, methods - impl 
```rust
struct Car {
    owner: String,
    year: u32,
    fuel_level: f32,
    price: u32,
}

impl Car {
    fn display_info(&self) {
        println!(
            "Owner: {}, Year: {}, Price: {}",
            self.owner, self.year, self.price
        );
    }
}

fn main() {
    let mut car_1 = Car {
        owner: String::from("Sword"),
        year: 2024,
        fuel_level: 55.0,
        price: 1_500_000,
    };

    car_1.display_info();
}
```

## Associated Method ( Static Function )
```rust
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
}
```