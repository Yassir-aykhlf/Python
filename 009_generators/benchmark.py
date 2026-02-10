import tracemalloc
import time

def run_benchmark():
    N = 1_000_000
    print(f"\n--- Memory Benchmark (N={N}) ---")

    tracemalloc.start()
    start_time = time.time()
    large_list = [x for x in range(N)]
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    duration = time.time() - start_time

    print("\nList Comprehension:")
    print(f"    Memory peak: {peak / 1024 / 1024:.2f} MB")
    print(f"    time to create: {duration:.4f} seconds")

    tracemalloc.start()
    start_time = time.time()
    large_gen = (x for x in range(N))
    _ = sum(large_gen)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    duration = time.time() - start_time

    print(f"\nGenerator Expression:")
    print(f"    Memory Peak: {peak / 1024 / 1024:.2f} MB")
    print(f"    Time to consume: {duration:.4f} seconds")

if __name__ == "__main__":
    run_benchmark()