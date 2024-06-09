//
//
//
//
//
//

fn main() {
    let num = 40;

    if num < 50 {
        println!("num is less than 50");
    } else {
        println!("num is equal or greater than 50");
    }

    let marks = 92;
    let mut grade = 'N';

    if marks >= 90 {
        grade = 'A';
    } else if marks >= 80 {
        grade = 'B';
    } else if marks >= 70 {
        grade = 'C';
    } else if marks >= 60 {
        grade = 'D';
    } else {
        grade = 'F';
    }

    grade = if marks >= 90 {
        'A'
    } else if marks >= 80 {
        'B'
    } else if marks >= 70 {
        'C'
    } else if marks >= 60 {
        'D'
    } else {
        println!("You failed!");
        'F'
    };

    // Pattern Matching
    match marks {
        90..=100 => {
            grade = 'A';
            println!("You got A!");
        }
        80..=89 => grade = 'B', // arm 2
        70..=79 => grade = 'C', // arm 3
        60..=69 => grade = 'D',
        _ => grade = 'F', // default arm, matches everything
    }

    grade = match marks {
        90..=100 => {
            println!("You got A!");
            'A'
        }
        80..=89 => 'B', // arm 2
        70..=79 => 'C', // arm 3
        60..=69 => 'D',
        _ => 'F', // default arm, matches everything
    };

    println!("Your grade: {grade}");
}
