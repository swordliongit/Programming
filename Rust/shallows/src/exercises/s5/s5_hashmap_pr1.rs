// Problem 1:
/* In this exercise, you will be working on creating a student management system
using Rust. The system should allow you to store and retrieve student information
based on their unique ID. For ease of work, the student structure is already
created in the code below

Next, create a StudentManager structure containing a field of student, which
will essentially be a hashmap where the key part will be an integer representing
unique ID of student and the value part will be the complete details of the
students contained in the student structure.

The StudentManager should implement the following methods:
1. new() -> Self: A constructor that initializes an empty student manager.

2. add_student(&mut self, student: Student) -> Result<(), String>:
Adds a student to the manager.
If the student's ID already exists, return an error message.
Otherwise, add the student to the manager and return Ok.

3. get_student(&self, id: i32) -> Option<&Student>: Retrieves a student
from the manager based on their ID.
If the student is found, return Some(student). Otherwise, return None.

Your task is to implement the StudentManager structure, and the mentioned methods.
Additionally, provide a sample usage of the student management system by adding
a few students and retrieving their information using the get_student() method.
*/

use std::collections::HashMap;

struct Student {
    id: i32,
    name: String,
    grade: String,
}

struct StudentManager {
    student_map: HashMap<i32, Student>,
}

impl StudentManager {
    fn new() -> StudentManager {
        StudentManager {
            student_map: HashMap::new(),
        }
    }

    fn add_student(&mut self, student: Student) -> Result<(), String> {
        // if self.student_map.contains_key(&student.id) {
        //     return Err("Student exists in DB".to_string());
        // } else {
        //     self.student_map.entry(student.id).or_insert(student);
        //     return Ok(());
        // }

        match self.student_map.get(&student.id) {
            Some(_) => Err("Student exists in DB".to_string()),
            None => {
                self.student_map.insert(student.id, student);
                Ok(())
            }
        }
    }

    fn get_student(&self, id: i32) -> Option<&Student> {
        // match self.student_map.get(&id) {
        //     Some(student) => Some(student),
        //     None => None,
        // }

        self.student_map.get(&id)
    }
}

fn main() {
    let mut manager = StudentManager::new();
    manager
        .add_student(Student {
            id: 123,
            name: String::from("Sword"),
            grade: String::from("99"),
        })
        .unwrap();

    let mut add_successful = manager.add_student(Student {
        id: 123,
        name: String::from("Sword"),
        grade: String::from("99"),
    });

    match add_successful {
        Ok(_) => println!("Student added successfully"),
        Err(msg) => println!("{}", msg),
    }

    match manager.get_student(123) {
        Some(student) => println!(
            "id: {}, name: {}, grade: {}",
            student.id, student.name, student.grade
        ),
        None => println!("Student doesn't exist in the DB!"),
    }
}
