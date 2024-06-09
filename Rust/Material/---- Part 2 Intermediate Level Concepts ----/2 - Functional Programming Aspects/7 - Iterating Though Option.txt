// -------------------------------------------
//          - Iterating Through Options
// -------------------------------------------

fn main() {
    // ------ Use case 1 -----

    let some_product = Some("laptop");
    let mut products = vec!["cellphone", "battery", "charger"];

    // Solution 1:
    // match some_product {
    //     Some(product) => products.push(product),
    //     _ => {}
    // };

    // Solution 2:
    // if let Some(product) = some_product {
    //     products.push(product);
    // }

    // Solution 3:
    products.extend(some_product);
    println!("{:?}", products);

    // ------- Use case 2 -----
    let mut products = vec!["cellphone", "battery", "charger"];
    let products_iter = products.iter().chain(some_product.iter());

    for prod in products_iter {
        println!("{:?} ", prod);
    }

    // ------ Use Case 3 -----
    let products = vec![Some("charger"), Some("battery"), None, Some("cellphone")];

    // Solution 1;
    // let mut prod_without_none = Vec::new();
    // for p in products {
    //     if p.is_some() {
    //         prod_without_none.push(p.unwrap());
    //     }
    // }

    // Solution 2:
    // let prod_without_none = products
    //     .into_iter()
    //     .filter(|x| x.is_some())
    //     .map(|x| x.unwrap())
    //     .collect::<Vec<&str>>();

    // Solution 3:
    let prod_wihtout_none: Vec<&str> = products.into_iter().flatten().collect();
    println!("{:?}", prod_wihtout_none);
}
