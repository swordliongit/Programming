# Commands

cargo new project_name
cargo build
cargo run
cargo build --release: for production
cargo login "token": To login crates.io
cargo doc --open: Shows published view of the package
cargo test
cargo publish, cargo publish --allow_dirty


# Code Organization
1. By default, src/ is the crate root. So main.rs and lib.rs are treated as default binary crates.
2. We can create additional binary crates under bin/ folder.
3. Select which binary to run with ==cargo run --bin "binary_name"==
4. 

## Packages
*  Managed through Cargo commands
*  Highest level of code organization
-  Contains Crates

## Rules
- Must have at least 1 crate
- At most 1 library crate
- Any number of binary crates

## Crates
- A compilation unit
- Can be a binary crate or a library crate
- Contains modules

## Modules
- Controls at a finer level, the structure, the visibility and privacy


![[Screenshot 2024-06-05 163757.png]]

---

# Modules
- By default, each module is private
- Sub-modules can access private Parent module items but Parents can't access private sub-module items
- Only Parent modules can access Public items of a Private sub-module
## Accessing other Modules

same crate:
```rust
mod product {
    pub struct Product {
        id: u64,
        name: String,
        price: f64,
        category: Category,
    }
...

mod order {
    struct Order {
        id: u64,
        product: crate::product::Product,
        customer: crate::customer::Customer,
        quantity: u32,
    }
...
```

---

## Simplifying long import names

```rust
mod product {
    use category::Category; // Import item
    pub struct Product {
        id: u64,
        name: String,
        price: f64,
        category: Category, // instead of category::Category
    }

    // sub module
    mod category {
        pub enum Category {
            Electronics,
            Clothing,
            Books,
        }
    }
...
```

---

## Visualizing Modules

1. cargo install cargo-modules
2. cargo modules structure (to target a specific binary: --lib, --bin)

Output:

```rust
crate test_package
├── mod customer: pub(crate)
│   └── struct Customer: pub
├── mod order: pub(crate)
│   └── struct Order: pub(self)
│       ├── fn calculate_discount: pub(self)
│       └── fn total_bill: pub(self)
└── mod product: pub(crate)
    ├── struct Product: pub
    │   ├── fn calculate_tax: pub(self)
    │   └── fn product_price: pub
    └── mod category: pub(self)
        └── enum Category: pub
```

---

## Modules based on files - Separating modules

*customer.rs*:
```rust
pub struct Customer {
    id: u64,
    name: String,
    email: String,
}
```

lib.rs:
```rust
mod customer; // forward declaration, found from the file name customer.rs

mod order {
    use crate::customer::Customer;
    use crate::product::Product;
    struct Order {
        id: u64,
        product: Product,
        customer: Customer,
        quantity: u32,
    }
...
```

### Sub-modules based on files

*lib.rs*: 
```rust
mod customer;
mod product;

mod order {
    use crate::customer::Customer;
    use crate::product::Product;
    struct Order {
        id: u64,
        product: Product,
        customer: Customer,
        quantity: u32,
    }
...
```

*product.rs*:
```rust
...
// sub module
mod category;
...
```

product/category.rs -> has to be put in a folder named as the parent module
```rust
pub enum Category {
    Electronics,
    Clothing,
    Books,
}
```

### Second Approach, mod files
- Each module has its own folder and a mod.rs file which includes the data

customer/mod.rs:
```rust
pub struct Customer {
    id: u64,
    name: String,
    email: String,
}
```

## Using/Exporting Modules in the Program

### Bad way, exposes the whole module with the ==pub== keyword
*lib.rs*: 
```rust
pub mod product { // has to be pub for this technique
    use category::Category;
    pub struct Product {
        id: u64,
        name: String,
        price: f64,
        category: Category,
    }
    ...
```

*main.rs*:
```rust
use test_package::{customer::Customer, product::Product};

fn main() {
    println!("Hello, world!");
}
```

### Recommended way, only exposing the necessary items
*lib.rs*:
```rust
pub use customer::Customer;
pub use product::{Category, Product};

mod product {
    pub use category::Category;
    pub struct Product {
        id: u64,
        name: String,
        price: f64,
        category: Category,
    }

```

*main.rs*:
```rust
use test_package::{Customer, Product, Category};

fn main() {
    println!("Hello, world!");
}
```

---

### Accessing Struct Fields of a Module
- Making the Struct itself pub, doesn't apply to its fields.
- Making the Enum itself pub, applies to its variants.

#### Approach 1: Making all the fields pub

*lib.rs*:
```rust
pub use customer::Customer;
pub use product::{Category, Product};

mod product {
    pub use category::Category;
    pub struct Product {
        pub id: u64,
        pub name: String,
        pub price: f64,
        pub category: Category,
    }
...
```

main.rs:
```rust
use test_package::{Category, Customer, Product};

fn main() {
    let product = Product {
        id: 245,
        name: String::from("Laptop"),
        price: 2500.0,
        category: Category::Electronics,
    };
}
```

#### Approach 2: Constructor method

*lib.rs*:
```rust
....
mod product {
    pub use category::Category;
    pub struct Product {
        id: u64,
        name: String,
        price: f64,
        category: Category,
    }

    impl Product {
        pub fn new(id: u64, name: String, price: f64, category: Category) -> Product {
            Product {
                id,
                name,
                price,
                category,
            }
        }
    }
....
```

## Example Re-Exports

1:
```rust
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

```

2:
```rust
mod University {
    pub struct Student {
        pub name: String, // fields need to be made public
        pub marks: u8,
        pub grade: char,
    }
}

use University::Student;

fn main() {
    let mut student_1 = Student {
        name: String::from("Alice"),
        marks: 75,
        grade: 'A',
    };
    println!("{} got {} grade", student_1.name, student_1.grade);
}
```

3:
```rust
mod seasons {
    pub enum Season {
        Spring,
        Summer,
        Autumn,
        Winter,
    }

    pub fn is_holiday(season: &Season) -> bool {
        match season {
            Season::Summer => true,
            _ => false,
        }
    }
}

use seasons::{is_holiday, Season};
fn main() {
    let current_season = Season::Autumn;
    if is_holiday(&current_season) {
        println!("It's a holiday season! Time for a vacation!");
    } else {
        println!("Regular work season. Keep hustling!");
    }
}
```

4:
```rust
mod m1 {
    struct A {
        d: m2::D,
    }
    pub mod m2 {  
    // private items of a private module are only accessible by the parents. 
    //we need to make the enum pub so that it can be used outside the parent module, 
    // i.e., module m3 in this case 
        pub enum D {
            B,
            C,
        }
    }
}

mod m3 {
    struct C {
        e: crate::m1::m2::D,
    }
}


fn main(){}
```

# External Dependencies


## array_tool crate example:
```rust
use test_package::{Category, Customer, Order, Product};

use array_tool::vec::*; // Bring all the items in vec module
fn main() {
    // let customer = Customer::new(1, String::from("Alice"), String::from("alice@mail.com"));
    // let order = Order::new(1, product, customer, 2);

    let product1 = Product::new(245, String::from("Laptop"), 2500.0, Category::Electronics);
    let product2 = Product::new(246, String::from("Book"), 100.0, Category::Books);
    let product3 = Product::new(247, String::from("Mouse"), 200.0, Category::Electronics);

    // println!("Cost of the order: {}", order.total_bill());

    let set1 = vec![&product1, &product2];
    let set2 = vec![&product2, &product3];
    let intersection = set1.intersect(set2);

    println!("{:?}", intersection);
}

```

# Publishing Your Crate

- cargo publish --allow_dirty to publish without the .git stuff

## Documentation Comments ///
- Private items won't show comments in the crates.io

```rust
mod product {
    pub use category::Category;
    #[derive(PartialEq, Debug)]
    /// Struct for Product related info
    pub struct Product {
        id: u64,
        name: String,
        price: f64,
        category: Category,
    }
```

## Section and Code Blocks

- cargo test: To execute the code block


```rust
...
	/// # Example Section
    /// ```
    /// use test_package::Category;
    /// use test_package::Product;
    /// let some_product  = Product::new(1, String::from("Laptop"), 899.999, Category::Electronics);
    /// assert_eq!(some_product.name, String::from("Laptop"));
    /// ```
    impl Product {
        pub fn new(id: u64, name: String, price: f64, category: Category) -> Product {
            Product {
                id,
                name,
                price,
                category,
            }
        }
    }
```

## Crate Root level Doc Comments //!
- Has to appear before any other item

```rust
//! # Online Business
//! This is a rust library for learning purposes
pub use customer::Customer;
pub use order::Order;
pub use product::{Category, Product};
...
```

