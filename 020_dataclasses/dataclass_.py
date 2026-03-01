from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

p1 = Point(0, 1)
p2 = Point(0, 1)
print(p1 == p2)
