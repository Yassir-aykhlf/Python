from __future__ import annotations
from functools import total_ordering 
from typing import Any

@total_ordering
class Money:
    amount: float
    currency: str

    def __init__(self, amount: float | int, currency: str) -> None:
        self.amount = float(amount)
        self.currency = currency

    def __repr__(self) -> str:
        return f'Money({self.amount!r}, {self.currency!r})'

    def __str__(self) -> str:
        return f'${self.amount} {self.currency}'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot compare different currencies")
            return self.amount < other.amount
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.amount, self.currency))

    def __add__(self, other: object) -> Money:
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"Currency mismatch: {self.currency} vs {other.currency}")
            return Money(self.amount + other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented

    def __mul__(self, other: object) -> Money:
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        raise TypeError(f"Unsupported operand type(s) for *: 'Money' and '{other.__class__.__name__}'")
        
    def __radd__(self, other: object) -> Money:
        return self.__add__(other)


    def __rmul__(self, other: object) -> Money:
        return self.__mul__(other)