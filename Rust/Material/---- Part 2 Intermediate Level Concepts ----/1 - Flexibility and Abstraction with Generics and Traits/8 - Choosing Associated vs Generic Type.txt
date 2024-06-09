// -----------------------------------------------------
// 		Choosing Associated vs Generic Types
// -----------------------------------------------------

trait Addition<Rhs, Output> {
    // type Rhs;
    // type Output;
    fn add(self, rhs: Rhs) -> Output;
}

struct Point {
    x: i32,
    y: i32,
}

impl Addition<Point, Point> for Point {
    fn add(self, rhs: Point) -> Point {
        Point {
            x: self.x + rhs.x,
            y: self.y + rhs.y,
        }
    }
}

impl Addition<i32, Point> for Point {
    fn add(self, rhs: i32) -> Point {
        Point {
            x: self.x + rhs,
            y: self.y + rhs,
        }
    }
}

struct Line {
    start: Point,
    end: Point,
}

impl Addition<Point, Line> for Point {
    fn add(self, rhs: Point) -> Line {
        Line {
            start: self,
            end: rhs,
        }
    }
}
fn main() {
    let p1 = Point { x: 1, y: 1 };
    let p2 = Point { x: 2, y: 2 };
    let p3: Point = p1.add(p2);

    assert_eq!(p3.x, 3);
    assert_eq!(p3.y, 3);

    let p1 = Point { x: 1, y: 1 };
    let p3 = p1.add(2);

    assert_eq!(p3.x, 3);
    assert_eq!(p3.y, 3);

    let p1 = Point { x: 1, y: 1 };
    let p2 = Point { x: 2, y: 2 };
    let line: Line = p1.add(p2);

    assert!(line.start.x == 1 && line.start.y == 1 && line.end.x == 2 && line.end.y == 2);
}
