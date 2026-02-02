# 01_object_model/memory_and_slots.py
"""
Object Internals and Memory Optimization

Demonstrates:
The memory cost of __dict__ vs __slots__
Object identity (is) vs Equality (==)
"""
import sys

class RegularPoint:
    """A standard class using __dict__ for attributes."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    """A memory-optimized class using __slots__."""
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def run_lab():
    print("--- Memory Comparison ---")
    p1 = RegularPoint(1, 2)
    p2 = SlottedPoint(1, 2)

    # getsizeof only measures the skeleton. The __dict__ is separate.
    base_size = sys.getsizeof(p1)
    dict_size = sys.getsizeof(p1.__dict__)
    
    print(f"RegularPoint total footprint (approx): {base_size + dict_size} bytes")
    print(f"SlottedPoint total footprint:          {sys.getsizeof(p2)} bytes")
    
    try:
        print(f"Slotted dict exists? {p2.__dict__}")
    except AttributeError:
        print("Verification: SlottedPoint has no __dict__ attribute.")

    print("\n--- Identity vs Equality ---")
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = list_a

    print(f"list_a == list_b: {list_a == list_b} (Same content)")
    print(f"list_a is list_b: {list_a is list_b} (Different objects - see IDs below)")
    print(f"ID(a): {id(list_a)}, ID(b): {id(list_b)}")
    print(f"list_a is list_c: {list_a is list_c} (Same object - Alias)")

if __name__ == "__main__":
    run_lab()