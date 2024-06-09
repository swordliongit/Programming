use test_package_swordlion::{Category, Customer, Order, Product};

use array_tool::vec::*;
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
