// -------------------------------------------
// 	   Option
// -------------------------------------------

struct Student {
    name: String,
    grade: Option<u32>,
}
fn get_grade(student_name: &String, student_db: &Vec<Student>) -> Option<u32> {
    for student in student_db {
        if student.name == *student_name {
            return student.grade;
        }
    }
    None
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

    let student_name = String::from("Bob");
    let student_grade = get_grade(&student_name, &student_db);

    // match student_grade {
    //     Some(grade) => println!("Grade is: {grade}"),
    //     None => {}
    // }

    if let Some(grade) = student_grade {
        println!("Grade is: {grade}");
    }
}

// enum Option<T> {
//     None,
//     Some(T),
// }
