// Problem 5:

/*
A Pythagorean triple consists of three positive integers a, b, and c, satisfying the condition a^2 + b^2 = c^2.
These triples are commonly written as (a, b, c), and a well-known example is (3, 4, 5).

Write a program that computes the Pythagorean triplet such that a < b < c and a + b + c = 1000.
*/

fn compute_pyth() {
    'outer: for a in 1..1000 {
        for b in a + 1..1000 {
            for c in b + 1..1000 {
                if a * a + b * b == c * c && a + b + c == 1000 {
                    println!("Pythagorean triple: {a}, {b}, {c}");
                    break 'outer;
                }
            }
        }
    }
}

fn main() {
    /* Your Code here */
    compute_pyth();
}
