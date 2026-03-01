"""Demonstrate Protocol usage."""
from typing import Protocol, runtime_checkable

@runtime_checkable
class Comparable(Protocol):
    def __lt__(self, other: 'Comparable') -> bool: ...


class Money:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __lt__(self, other: 'Comparable') -> bool:
        if isinstance(other, Money):
            return self.amount < other.amount
        return NotImplemented


money = Money(10.0)
print(isinstance(money, Comparable)) # yes it is