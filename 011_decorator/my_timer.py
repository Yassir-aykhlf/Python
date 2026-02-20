import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"time: {end - start:.6f} seconds")
        return result
    return wrapper        

@timer
def heavy_computation(n: int) -> int:
    total = sum(i * i for i in range(n))
    return total

if __name__ == "__main__":
    calculated_total = heavy_computation(1_000_000)
    print(f"Total is: {calculated_total}")