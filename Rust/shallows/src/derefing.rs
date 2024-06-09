fn main() {
    let mut data = 100;
    let ref_1 = &mut data;
    let copied_data = *ref_1; // copied
    *ref_1 = 15; // copied_data not affected

    let mut heap_data = vec![1, 200, 232];
    let ref_2 = &mut heap_data;
    // let copied_heap_data = *ref_2; // doesn't work
    // let copied_heap_data = ref_2.clone(); // works

    let s1: String = String::from("Hello");
    let r1: &String = &s1;
    let r2: &&String = &r1;
    let r3: &&&String = &r2;
    let sr3 = r3.to_string();
    println!("{}", { sr3 == "Hello".to_string() });
}
