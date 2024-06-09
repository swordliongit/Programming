// -------------------------------------------
//	 Ownership in Functions
// -------------------------------------------

fn main() {
    let vec_1 = vec![1, 2, 3];
    takes_ownership(vec_1.clone());
    println!("vec 1 is: {:?}", vec_1);

    let vec_2 = gives_onwership();
    println!("vec 2 is: {:?}", vec_2);

    let vec_3 = takes_and_gives_ownership(vec_2);
    //println!("vec 2 is: {:?}", vec_2);
    println!("vec 3 is: {:?}", vec_3);

    let x = 10;
    stack_function(x);
    println!("In main, x is: {x}");
}

fn takes_ownership(vec: Vec<i32>) {
    println!("vec is: {:?}", vec);
}

fn gives_onwership() -> Vec<i32> {
    vec![4, 5, 6]
}

fn takes_and_gives_ownership(mut vec: Vec<i32>) -> Vec<i32> {
    vec.push(10);
    vec
}

fn stack_function(mut var: i32) {
    var = 56;
    println!("In func, var is: {var}");
}
