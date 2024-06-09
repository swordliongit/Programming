// -------------------------------------------
// 		RefCell Example
// -------------------------------------------
use std::{cell::RefCell, rc::Rc};

#[derive(Debug)]
struct File {
    active_user: u32,
}

#[derive(Debug)]
struct User {
    file: Rc<RefCell<File>>,
}

fn main() {
    let mut txt_file = Rc::new(RefCell::new((File { active_user: 0 })));

    let mut user_1 = User {
        file: Rc::clone(&txt_file),
    };
    user_1.file.borrow_mut().active_user += 1;
    println!("Active users: {:?}", txt_file.borrow().active_user);

    let mut user_2 = User {
        file: Rc::clone(&txt_file),
    };
    user_2.file.borrow_mut().active_user += 1;
    println!("Active users: {:?}", txt_file.borrow().active_user);
}
