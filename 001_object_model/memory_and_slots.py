import sys

class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

print("--- Memory Comparison ---")
p1 = RegularPoint(1, 2)
p2 = SlottedPoint(1, 2)

# note: getsizeof only measures the skeleton. The __dict__ is separate.
base_size = sys.getsizeof(p1)
dict_size = sys.getsizeof(p1.__dict__)

print(f"RegularPoint total footprint (approx): {base_size + dict_size} bytes")
print(f"SlottedPoint total footprint:          {sys.getsizeof(p2)} bytes")

try:
    print(f"Slotted dict exists? {p2.__dict__}")
except AttributeError:
    print("Verification: SlottedPoint has no __dict__ attribute.")