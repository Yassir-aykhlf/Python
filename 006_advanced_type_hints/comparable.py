from typing import Protocol, TypeVar, Any

class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool:
        ...

C = TypeVar("C", bound=Comparable)

def max_item(a: C, b: C) -> C:
    if a < b:
        return b
    return a

print(max_item(1, 2))
print(max_item("apple", "banana"))