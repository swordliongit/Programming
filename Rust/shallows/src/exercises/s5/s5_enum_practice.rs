// Problem 1:
/* You are tasked with implementing a library management system using Rust.
Your goal is to design a program that can handle books and magazines.
To fulfill the requirements, follow the steps below:

Create a structure called Item with the following fields:
id: An integer representing the unique identifier of the item.
title: A string representing the title of the item.
year: An integer representing the publication year of the item.
type: an enumeration type. The details are coming below.

Create an enumeration called ItemType with two variants:
Book: Represents a book.
Magazine: Represents a magazine.

Implement a function called display_item_info() that takes an Item as input
and displays its information. The function should output
the item's ID, title, publication year, and type (book or magazine).
*/

struct Item {
    id: u32,
    title: String,
    year: u32,
    variant: ItemType,
}

impl Item {
    fn display_item_info(&self) {
        println!(
            "Id: {}, Title: {}, Pub. year: {}, Type: {:?}",
            self.id, self.title, self.year, self.variant
        );
    }
}

#[derive(Debug)]
enum ItemType {
    Book,
    Magazine,
}

fn main() {
    let book_1 = Item {
        id: 145,
        title: "Concurrency in Action".to_string(),
        year: 2019,
        variant: ItemType::Book,
    };

    book_1.display_item_info();
}
