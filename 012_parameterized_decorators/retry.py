"""A parameterized decorator that retries a function upon encountering specified exceptions."""
import time
from functools import wraps
from typing import Callable, Any, Type, Tuple, TypeVar, cast


F = TypeVar('F', bound=Callable[..., Any])

def retry(
    attempts: int = 3,
    delay: float = 1.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable[[F], F]:
    """
    Retries a function upon encountering specified exceptions.
    """
    if not isinstance(attempts, int) or attempts <= 0:
        raise ValueError(f"attempts must be a positive integer, got {attempts}")
    if not isinstance(delay, (int, float)) or delay < 0:
        raise ValueError(f"delay must be a non-negative number, got {delay}")
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == attempts:
                        raise
                    time.sleep(delay)
            raise RuntimeError("Unreachable code reached in retry decorator.")
        return cast(F, wrapper)
    return decorator

if __name__ == "__main__":
    import random

    @retry(attempts=5, delay=1.5, exceptions=(ValueError,))
    def unreliable_function() -> str:
        """Dummy function that fails randomly."""
        if random.random() < 0.8:
            raise ValueError("Random failure!")
        return "Success!"
    print(unreliable_function())
