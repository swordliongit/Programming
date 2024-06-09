use benchmark_testing::{sort_algo_1, sort_algo_2};
use criterion::{criterion_group, criterion_main, Bencher, Criterion};

fn sort_benchmark(c: &mut Criterion) {
    let mut numbers = vec![
        1, 2, 3, 4, 5, 6, 10, 2, 22, 100, 123, 144, 155, 222, 95, 23, 5, 5, 5, 2, 3, 4, 10,
    ];

    c.bench_function("Sorting Algorithm", |b: &mut Bencher| {
        b.iter(|| sort_algo_2(&mut numbers))
    });
}

criterion_group!(benches, sort_benchmark);
criterion_main!(benches);
