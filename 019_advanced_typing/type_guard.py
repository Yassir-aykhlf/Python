from typing import TypeGuard

def is_string_list(val: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

def process_data(data: list[object]):
    if is_string_list(data):
        print(data[0].upper())
