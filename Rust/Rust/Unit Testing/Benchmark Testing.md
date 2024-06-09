1. Configure cargo.toml for Criterion:
```toml
[package]
name = "benchmark_testing"
version = "0.1.0"
edition = "2021"

[dependencies]
criterion = "0.4.0"

[[bench]]
name = "sorting_benchmark"
harness = false
```

2. Create top level directory "benches/sorting_benchmark.rs"
*lib.rs:*
```rust
pub fn sort_algo_1<T: PartialOrd>(arr: &mut Vec<T>) {
    let mut swapped = false;
    for i in 0..(arr.len() - 1) {
        if arr[i] > arr[i + 1] {
            arr.swap(i, i + 1);
            swapped = true;
        }
    }
    if swapped {
        sort_algo_1(arr);
    }
}

pub fn sort_algo_2<T: Ord>(arr: &mut Vec<T>) {
    let len = arr.len();
    for left in 0..len {
        let mut smallest = left;
        for right in (left + 1)..len {
            if arr[right] < arr[smallest] {
                smallest = right;
            }
        }
        arr.swap(smallest, left);
    }
}
```

==sorting_benchmark.rs:==
```rust
use benchmark_testing::{sort_algo_1, sort_algo_2};
use criterion::{criterion_group, criterion_main, Bencher, Criterion};

fn sort_benchmark(c: &mut Criterion) {
    let mut numbers = vec![
        1, 2, 3, 4, 5, 6, 10, 2, 22, 100, 123, 144, 155, 222, 95, 23, 5, 5, 5, 2, 3, 4, 10,
    ];

    c.bench_function("Sorting Algorithm", |b: &mut Bencher| {
        b.iter(|| sort_algo_1(&mut numbers))
    });
}

criterion_group!(benches, sort_benchmark);
criterion_main!(benches);
```

3. Run ==cargo bench== and examine results