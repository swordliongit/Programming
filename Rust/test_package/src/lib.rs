// mod customer;
// mod product;
// mod order;
// use crate::product::category;
//! # Online Business
//! This is a rust library for learning purposes
pub use customer::Customer;
pub use order::Order;
pub use product::{Category, Product};

/// Product module -> Private, invisible in crates.io
mod product {
    pub use category::Category;
    #[derive(PartialEq, Debug)]
    /// Struct for Product related info
    pub struct Product {
        id: u64,
        pub name: String,
        price: f64,
        category: Category,
    }

    /// # Example Section
    /// ```
    /// use test_package_swordlion::Category;
    /// use test_package_swordlion::Product;
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

    mod category {
        #[derive(PartialEq, Debug)]
        /// Enum for Product categories
        pub enum Category {
            Electronics,
            Clothing,
            Books,
        }
    }

    impl Product {
        fn calculate_tax(&self) -> f64 {
            self.price * 0.1
        }

        pub fn product_price(&self) -> f64 {
            self.price + self.calculate_tax()
        }
    }
}

mod customer {
    #[derive(PartialEq)]
    /// Struct for customer related info
    pub struct Customer {
        id: u64,
        name: String,
        email: String,
    }

    impl Customer {
        pub fn new(id: u64, name: String, email: String) -> Customer {
            Customer { id, name, email }
        }
    }
}

mod order {
    use crate::customer::Customer;
    use crate::product::Product;
    #[derive(PartialEq)]
    /// Struct for Ordering Products
    pub struct Order {
        id: u64,
        product: Product,
        customer: Customer,
        quantity: u32,
    }

    impl Order {
        pub fn new(id: u64, product: Product, customer: Customer, quantity: u32) -> Order {
            Order {
                id,
                product,
                customer,
                quantity,
            }
        }

        fn calculate_discount(&self) -> f64 {
            if self.quantity > 5 {
                0.1
            } else {
                0.0
            }
        }

        pub fn total_bill(&self) -> f64 {
            let discount = self.calculate_discount();
            let total_before_discount = self.product.product_price() * self.quantity as f64;
            total_before_discount - (total_before_discount * discount)
        }
    }
}
