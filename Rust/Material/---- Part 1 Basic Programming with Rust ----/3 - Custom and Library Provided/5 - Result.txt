// -------------------------------------------
// 			    Option
// -------------------------------------------

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
//     None // not reachable
// }
// enum Result<T, E> {
//     Ok(T),
//     Err(E),
// }

// fn check_student(student_name: &String, student_db: &Vec<Student>) -> Result<(), String> {
//     for student in student_db {
//         if student.name == *student_name {
//             return Ok(());
//         }
//     }
//     Err(String::from("Student not found"))
// }

fn check_student_get_grade(
    student_name: &String,
    student_db: &Vec<Student>,
) -> Result<Option<u32>, String> {
    for student in student_db {
        if student.name == *student_name {
            return Ok(student.grade);
        }
    }
    Err(String::from("Student not found"))
}
fn main() {
    let student_db = vec![
        Student {
            name: String::from("Alice"),
            grade: Some(95),
        },
        Student {
            name: String::from("Bob"),
            grade: Some(87),
        },
        Student {
            name: String::from("Charlie"),
            grade: None,
        },
    ];

    let student_name = String::from("Adam");
    let student_status = check_student_get_grade(&student_name, &student_db);

    match student_status {
        Ok(option_grade) => {
            if let Some(grade) = option_grade {
                println!("Grade is: {grade}");
            }
        }
        Err(error_msg) => println!("{error_msg}"),
    }
    // let student_grade = get_grade(&student_name, &student_db);

    // match student_grade {
    //     Some(grade) => println!("Grade is: {grade}"),
    //     None => {}
    // }

    // if let Some(grade) = student_grade {
    //     println!("Grade is: {grade}");
    // }
}
