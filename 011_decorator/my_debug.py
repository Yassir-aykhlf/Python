from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f"[DEBUG] calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} returned {repr(result)}")
        return result
    return wrapper

@debug
def configure_subsystem(system_id, mode="safe", retries=3):
    return True

configure_subsystem(42, retries=5)