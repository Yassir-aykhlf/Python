from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        frozen_kwargs = tuple(sorted(kwargs.items()))
        cache_key = (args, frozen_kwargs)
        if cache_key in cache:
            return cache[cache_key]
        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result
    return wrapper