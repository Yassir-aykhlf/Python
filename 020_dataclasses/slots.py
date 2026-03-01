from dataclasses import dataclass
from objsize import get_deep_size

@dataclass(slots=True)
class OptimizedPoint:
    x: float
    y: float

@dataclass
class Point:
    x: float
    y: float

p1 = OptimizedPoint(1, 10)
p2 = Point(1, 10)

print(f"optimized Point size: {get_deep_size(p1)}")
print(f"unoptimized Point size: {get_deep_size(p2)}") #4x