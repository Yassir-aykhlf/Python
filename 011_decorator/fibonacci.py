from my_memoize import memoize
from my_timer import timer

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# non-memoized version
@timer
def run():
    return fibonacci(20)


# memoized version
@memoize
def fibonacci_memoized(n):
    if n < 2:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


@timer
def run_memoized():
    return fibonacci_memoized(20)


if __name__ == "__main__":
    print(f"non-memoized result: {run()}")
    print(f"memoized result: {run_memoized()}")
