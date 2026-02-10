from typing import overload

@overload
def process(value: int) -> str:
    ...

@overload
def process(value: str) -> int:
    ...

def process(value: int | str) -> str | int:
    if isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        return len(value)
    raise TypeError("Invalid Type")