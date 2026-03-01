from dataclasses import dataclass, field

@dataclass
class Order:
    price: int
    items: list[str] = field(default_factory=list)

order1 = Order(10)
order1.items.append('apple')

order2 = Order(5)
print(order1)
print(order2)
