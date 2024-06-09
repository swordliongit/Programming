use test_package_swordlion::{Category, Customer, Order, Product};
mod helper;
#[test]
fn test_total_bill_without_discount() {
    helper::common_setup();
    let product = Product::new(1, String::from("Book"), 19.9, Category::Books);
    let customer = Customer::new(1, String::from("Mark"), String::from("mark@zuck.com"));
    let order = Order::new(2, product, customer, 3);

    assert_eq!(format!("{:.2}", order.total_bill()), "65.67");
}

#[test]
fn test_total_bill_with_discount() {
    let product = Product::new(1, String::from("Book"), 19.99, Category::Books);
    let customer = Customer::new(1, String::from("Mark"), String::from("mark@zuck.com"));
    let order = Order::new(2, product, customer, 10);

    assert_eq!(format!("{:.2}", order.total_bill()), "197.90");
}
