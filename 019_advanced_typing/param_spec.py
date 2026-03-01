import time
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec('P')
R = TypeVar('R')

def timer(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Executed in {end - start:.4f}s")
        return result
    return wrapper

@timer
def heavy_computation(x: int, y: int) -> str:
    time.sleep(1)
    return str(x + y)

res = heavy_computation(5, 10)
