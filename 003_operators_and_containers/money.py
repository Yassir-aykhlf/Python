from functools import total_ordering 

@total_ordering
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f'Money({self.amount!r}, {self.currency!r})'

    def __str__(self):
        return f'${self.amount} {self.currency}'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.amount == other.amount and self.currency == other.currency
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            if self.currency != other.currency:
                raise ValueError("Cannot compare different currencies")
            return self.amount < other.amount
        return NotImplemented

    def __hash__(self):
        return hash((self.amount, self.currency))

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self.currency != other.currency:
                raise ValueError(f"Currency mismatch: {self.currency} vs {other.currency}")
            return Money(self.amount + other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        raise TypeError(f"Unsupported operand type(s) for *: 'Money' and '{other.__class__.__name__}'")
        
    def __radd__(self, other):
        return self.__add__(other)


    def __rmul__(self, other):
        return self.__mul__(other)