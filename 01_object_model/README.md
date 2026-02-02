# 01. Python Object Model

## Key Concepts

### 1. Everything is an Object
Variables in Python are not boxes that contain values; they are references to objects in memory.

### 2. Identity vs Equality
- **Equality (`==`)**: Checks if the *values* of two objects are the same.
- **Identity (`is`)**: Checks if two variables refer to the *exact same object* in memory (compares `id()`).

### 3. Mutability & The "Tuple Paradox"
- **Immutable**: `int`, `str`, `tuple`, `frozenset`. (Modifying creates a new object).
- **Mutable**: `list`, `dict`, `set`, `bytearray`. (Modifying changes the object in-place).
- **Tuple**: A tuple is immutable, but if it holds a mutable object, that inner object can still be changed. Immutability is "shallow".

### 4. Memory Optimization (`__slots__`)
- **Standard Classes**: Store attributes in a `__dict__` (hash table), which consumes significant RAM per object.
- **Slotted Classes**: Using `__slots__ = ('x', 'y')` replaces `__dict__` with a fixed-size C-array structure. This denies dynamic attribute creation but saves massive amounts of memory for millions of small objects.

### 5. Aliasing & Magic Methods
- **Aliasing**: Assigning a mutable object to a new variable - or passing it to a function - copies the *reference*, not the data. Changes affect all aliases.
- **`__repr__` vs `__str__`**:
  - `__str__`: Readable string for end-users.
  - `__repr__`: Unambiguous string for developers (should ideally look like source code).