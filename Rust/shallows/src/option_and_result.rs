//
//
//
//
//
//
// enum Option<T> {
//     None,
//     Some(T),
// }

// enum Result<E, T> {
//     Ok(T),
//     Err(E),
// }

struct Student {
    name: String,
    grade: Option<u32>,
}

// fn get_grade(student_name: &String, student_db: &Vec<Student>) -> Option<u32> {
//     for student in student_db {
//         if student.name == *student_name {
//             return student.grade;
//         }
//     }
//     None
// }

// fn check_grade(student_name: &String, student_db: &Vec<Student>) -> Result<(), String> {
//     for student in student_db {
//         if student.name == *student_name {
//             return Ok(());
//         }
//     }
//     Err(String::from("Student not found!"))
// }

fn check_grade(student_name: &String, student_db: &Vec<Student>) -> Result<Option<u32>, String> {
    for student in student_db {
        if student.name == *student_name {
            return Ok(student.grade);
        }
    }
    Err(String::from("Student not found!"))
}

fn main() {
    let student_db = vec![
        Student {
            name: String::from("Sword"),
            grade: Some(78),
        },
        Student {
            name: String::from("Lion"),
            grade: Some(90),
        },
        Student {
            name: String::from("Contra"),
            grade: None,
        },
    ];

    let student_name = String::from("Lion");
    let student_status = check_grade(&student_name, &student_db);

    match student_status {
        Ok(student_grade) => {
            if let Some(grade) = student_grade {
                println!("{}'s grade is {}", student_name, grade);
            }
        }
        Err(error_msg) => println!("{error_msg}"),
    }

    // match student_grade {
    //     Some(grade) => println!("{}'s grade is {}", student_name, grade),
    //     None => {}
    // }
}
