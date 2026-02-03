class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def __repr__(self):
        return f'Money({self.amount!r}, {self.currency!r})'
    def __str__(self):
        return f'${self.amount} {self.currency}'
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency
    def __hash__(self):
        return hash((self.amount, self.currency))

m1 = Money(10, 'USD')
m2 = Money(10, 'USD')
wallet = { m1: "Lunch" }

print(f"Equal? {m1 == m2}")
print(f"Safety check? {m1 != "m2"}")
print(f"Hashable? {m2 in wallet}")